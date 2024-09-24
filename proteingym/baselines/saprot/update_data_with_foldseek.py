import os
import argparse

import pandas as pd

from foldseek_util import get_struc_seq


def main():
    """
    Main script to add foldseek sequences to DMS data csv files.
    """
    parser = argparse.ArgumentParser(description='Add foldseek sequences to data')
    parser.add_argument('--foldseek_bin',
                        default="",
                        type=str, help='Path to foldseek binary file')
    parser.add_argument('--DMS_reference_file_path',
                        default='',
                        type=str, help='Path of DMS reference file')
    parser.add_argument('--DMS_data_folder',
                        default='',
                        type=str, help='Path of DMS folder')
    parser.add_argument('--structure_data_folder', default='', type=str, help='Path of structure folder')
    parser.add_argument('--output_folder', default=None, type=str,
                        help='Path of folder to write output CSVs to')
    args = parser.parse_args()
    
    mapping_protein_seq_DMS = pd.read_csv(args.DMS_reference_file_path)
    DMS_id_list = mapping_protein_seq_DMS["DMS_id"]
    for DMS_id in DMS_id_list:
        # skip BRCA2_HUMAN for now because it has multiple pdb files for its structure.
        if "BRCA2_HUMAN" in DMS_id:
            continue
        output_file = args.output_folder + os.sep + DMS_id + '.csv'
        
        print("Processing DMS_Id: {}".format(DMS_id))
        DMS_file_name = mapping_protein_seq_DMS["DMS_filename"][mapping_protein_seq_DMS["DMS_id"] == DMS_id].values[0]
        
        DMS_data = pd.read_csv(args.DMS_data_folder + os.sep + DMS_file_name, low_memory=False)
        
        pdb_file_name = mapping_protein_seq_DMS["pdb_file"][mapping_protein_seq_DMS["DMS_id"] == DMS_id].values[0]
        pdb_file = args.structure_data_folder + os.sep + pdb_file_name
        foldseek_seq = get_struc_seq(foldseek=args.foldseek_bin, path=pdb_file, chains=["A"])["A"][1].upper()
        print("foldseek_seq: {}".format(foldseek_seq))
        print()
        DMS_data['foldseek'] = foldseek_seq 
        DMS_data.to_csv(output_file, index=False)


if __name__ == '__main__':
    main()