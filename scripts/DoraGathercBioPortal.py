import argparse
from targetexplorer.cBioPortal import GatherCbioportalData, external_data_filepath


argparser = argparse.ArgumentParser(description='Gather cBioPortal data')
argparser.add_argument(
    '--use_existing_data',
    help='Only works if an existing file {0} is present.'.format(external_data_filepath),
    action='store_true',
    default=False
)
args = argparser.parse_args()

GatherCbioportalData(use_existing_data=args.use_existing_data)