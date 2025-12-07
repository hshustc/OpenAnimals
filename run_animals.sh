# Training
CUDA_VISIBLE_DEVICES=1 python3 tools/train_net.py --dist-url tcp://127.0.0.1:29506 --num-gpus 1 --config-file ./configs/Animals-ARBase3/bagtricks_R50_NORandomErasing_MGN12.yml \
    DATASETS.NAMES "('Animals-HyenaID2022',)" DATASETS.TESTS  "('Animals-HyenaID2022',)" OUTPUT_DIR logs/Animals-HyenaID2022/bagtricks_R50_NORandomErasing_MGN12.yml

CUDA_VISIBLE_DEVICES=2 python3 tools/train_net.py --dist-url tcp://127.0.0.1:29506 --num-gpus 1 --config-file ./configs/Animals-ARBase3/bagtricks_R50_NORandomErasing_MGN12.yml \
    DATASETS.NAMES "('Animals-LeopardID2022',)" DATASETS.TESTS  "('Animals-LeopardID2022',)" OUTPUT_DIR logs/Animals-LeopardID2022/bagtricks_R50_NORandomErasing_MGN12.yml

CUDA_VISIBLE_DEVICES=3 python3 tools/train_net.py --dist-url tcp://127.0.0.1:29506 --num-gpus 1 --config-file ./configs/Animals-ARBase3/bagtricks_R50_NORandomErasing_MGN12.yml \
    DATASETS.NAMES "('Animals-SeaTurtleIDHeads',)" DATASETS.TESTS  "('Animals-SeaTurtleIDHeads',)" OUTPUT_DIR logs/Animals-SeaTurtleIDHeads/bagtricks_R50_NORandomErasing_MGN12.yml

CUDA_VISIBLE_DEVICES=4 python3 tools/train_net.py --dist-url tcp://127.0.0.1:29506 --num-gpus 1 --config-file ./configs/Animals-ARBase3/bagtricks_R50_NORandomErasing_MGN12.yml \
    DATASETS.NAMES "('Animals-WhaleSharkID',)" DATASETS.TESTS  "('Animals-WhaleSharkID',)" OUTPUT_DIR logs/Animals-WhaleSharkID/bagtricks_R50_NORandomErasing_MGN12.yml


# Validation
CUDA_VISIBLE_DEVICES=1 python3 tools/train_net.py --eval-only --config-file ./configs/Animals-ARBase3/bagtricks_R50_NORandomErasing_MGN12.yml \
    DATASETS.NAMES "('Animals-HyenaID2022',)" DATASETS.TESTS  "('Animals-HyenaID2022',)" MODEL.WEIGHTS logs/Animals-HyenaID2022/bagtricks_R50_NORandomErasing_MGN12.yml/model_final.pth

CUDA_VISIBLE_DEVICES=2 python3 tools/train_net.py --eval-only --config-file ./configs/Animals-ARBase3/bagtricks_R50_NORandomErasing_MGN12.yml \
    DATASETS.NAMES "('Animals-LeopardID2022',)" DATASETS.TESTS  "('Animals-LeopardID2022',)" MODEL.WEIGHTS logs/Animals-LeopardID2022/bagtricks_R50_NORandomErasing_MGN12.yml/model_final.pth
    
CUDA_VISIBLE_DEVICES=3 python3 tools/train_net.py --eval-only --config-file ./configs/Animals-ARBase3/bagtricks_R50_NORandomErasing_MGN12.yml \
    DATASETS.NAMES "('Animals-SeaTurtleIDHeads',)" DATASETS.TESTS  "('Animals-SeaTurtleIDHeads',)" MODEL.WEIGHTS logs/Animals-SeaTurtleIDHeads/bagtricks_R50_NORandomErasing_MGN12.yml/model_final.pth

CUDA_VISIBLE_DEVICES=4 python3 tools/train_net.py --eval-only --config-file ./configs/Animals-ARBase3/bagtricks_R50_NORandomErasing_MGN12.yml \
    DATASETS.NAMES "('Animals-WhaleSharkID',)" DATASETS.TESTS  "('Animals-WhaleSharkID',)" MODEL.WEIGHTS logs/Animals-WhaleSharkID/bagtricks_R50_NORandomErasing_MGN12.yml/model_final.pth
