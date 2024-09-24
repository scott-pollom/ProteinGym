#!/bin/bash

python3 ../../proteingym/baselines/saprot/update_data_with_foldseek.py \
            --foldseek_bin /Users/spollom/Desktop/ProteinGymData/foldseek/bin/foldseek \
            --DMS_reference_file_path /Users/spollom/Desktop/ProteinGymData/DMS_substitutions.csv \
            --DMS_data_folder /Users/spollom/Desktop/ProteinGymData/DMS_ProteinGym_substitutions \
            --structure_data_folder /Users/spollom/Desktop/ProteinGymData/ProteinGym_AF2_structures \
            --output_folder /Users/spollom/Desktop/ProteinGymData/DMS_ProteinGym_substitutions_with_foldseek
