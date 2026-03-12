#!/usr/bin/env python3
"""TxGNN 馬來西亞藥品老藥新用預測 - 深度學習方法

此腳本使用 TxGNN 預訓練模型執行深度學習預測，
自動偵測可用的運算裝置（CUDA/CPU）。
支援中斷續算：中途按 Ctrl+C 中斷後，重新執行會自動從上次中斷處繼續。

前置條件:
    1. model_ckpt/ 目錄已有預訓練模型
    2. 設定 conda 環境

使用方法:
    # 啟動 conda 環境並執行
    conda activate txgnn
    python scripts/run_txgnn_prediction.py

    # 忽略之前的進度，重新開始
    python scripts/run_txgnn_prediction.py --restart

環境設定:
    conda create -n txgnn python=3.11 -y
    conda activate txgnn
    pip install torch==2.2.2 torchvision==0.17.2
    pip install dgl==1.1.3
    pip install git+https://github.com/mims-harvard/TxGNN.git
    pip install pandas tqdm pyyaml pydantic ogb
"""

import argparse
import sys
from pathlib import Path

# 將 src 加入 Python 路徑
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from mytxgnn.predict.txgnn_model import (
    check_dependencies,
    detect_device,
    print_install_instructions,
    CheckpointManager,
    TxGNNPredictor,
)

import pandas as pd


def run_malaysia_drug_prediction(
    drug_mapping_path: Path = None,
    output_path: Path = None,
    device: str = None,
    min_score: float = 0.0,
    top_k_per_drug: int = None,
    restart: bool = False,
    checkpoint_path: Path = None,
) -> pd.DataFrame:
    """執行馬來西亞藥品老藥新用預測

    Args:
        drug_mapping_path: 藥品映射 CSV 路徑
        output_path: 輸出結果路徑
        device: 運算裝置
        min_score: 最低分數門檻
        top_k_per_drug: 每個藥物保留前 k 個疾病
        restart: 是否忽略之前的進度重新開始
        checkpoint_path: Checkpoint 檔案路徑

    Returns:
        預測結果 DataFrame
    """
    base_dir = Path(__file__).parent.parent

    # 預設路徑
    if drug_mapping_path is None:
        drug_mapping_path = base_dir / "data" / "processed" / "drugbank_mapping.csv"
    if output_path is None:
        output_path = base_dir / "data" / "processed" / "txgnn_dl_predictions.csv"
    if checkpoint_path is None:
        checkpoint_path = base_dir / "data" / "processed" / "txgnn_checkpoint.csv"

    # 初始化 checkpoint 管理器
    checkpoint_manager = CheckpointManager(checkpoint_path)

    # 如果指定重新開始，清除 checkpoint
    if restart:
        checkpoint_manager.clear()
        print("已清除之前的進度，將從頭開始預測")
    else:
        # 載入之前的進度
        checkpoint_manager.load()

    # 載入藥品映射
    print(f"載入藥品映射: {drug_mapping_path}")
    drug_mapping = pd.read_csv(drug_mapping_path)
    print(f"共 {len(drug_mapping)} 筆藥品資料")

    # 初始化預測器
    predictor = TxGNNPredictor(device=device)
    predictor.setup()

    # 執行預測（使用 checkpoint 管理器）
    predictions = predictor.predict_batch(
        drug_mapping,
        min_score=min_score,
        top_k_per_drug=top_k_per_drug,
        checkpoint_manager=checkpoint_manager,
    )

    print(f"\n預測完成！共 {len(predictions)} 筆結果")

    # 輸出預測結果
    if len(predictions) > 0:
        result = predictions.rename(columns={
            "disease_name": "potential_indication",
        })
        result["source"] = "TxGNN Deep Learning Model"

        # 儲存結果
        result.to_csv(output_path, index=False, encoding="utf-8")
        print(f"結果已儲存至: {output_path}")

        # 印出統計
        print("\n" + "=" * 50)
        print("TxGNN 深度學習預測統計摘要")
        print("=" * 50)
        print(f"總預測數: {len(result)}")
        print(f"涉及藥物數: {result['drugbank_id'].nunique()}")
        print(f"涉及適應症數: {result['potential_indication'].nunique()}")
        print(f"平均信心分數: {result['txgnn_score'].mean():.4f}")
        print(f"最高信心分數: {result['txgnn_score'].max():.4f}")

        return result

    return predictions


def main():
    parser = argparse.ArgumentParser(description="TxGNN Malaysia Drug Repurposing Prediction")
    parser.add_argument(
        "--restart",
        action="store_true",
        help="忽略之前的進度，重新開始預測",
    )
    parser.add_argument(
        "--check-deps",
        action="store_true",
        help="只檢查依賴套件是否已安裝",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("TxGNN Malaysia Drug Repurposing Prediction")
    print("=" * 60)
    print()

    # 偵測裝置
    device = detect_device()

    # 檢查依賴
    deps_ok, missing = check_dependencies()

    if args.check_deps:
        if deps_ok:
            print("✓ 所有依賴套件已安裝")
        else:
            print(f"✗ 缺少套件: {', '.join(missing)}")
            print_install_instructions(missing, device)
        return

    if not deps_ok:
        print(f"\n缺少必要套件: {', '.join(missing)}")
        print_install_instructions(missing, device)
        print("\n請安裝上述套件後重新執行此腳本。")
        sys.exit(1)

    print()

    # 執行預測（支援中斷續算）
    result = run_malaysia_drug_prediction(
        device=device,
        min_score=0.0,
        restart=args.restart,
    )

    if result is not None and len(result) > 0:
        print("\n預測完成！")
        print(f"結果檔案: data/processed/txgnn_dl_predictions.csv")
        print(f"Checkpoint: data/processed/txgnn_checkpoint.csv")
    else:
        print("\n預測未產生結果，請檢查藥品映射資料。")


if __name__ == "__main__":
    main()
