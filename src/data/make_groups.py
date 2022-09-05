import click
import logging
# from pathlib import Path
# from dotenv import find_dotenv, load_dotenv
import json


@click.command()
@click.option('--input_group_path', type=click.Path())
@click.option('--output_group_path', type=click.Path())
@click.option('--output_mcc_path', type=click.Path())
def main(input_group_path, output_group_path, output_mcc_path):
	logger = logging.getLogger(__name__)
	logger.info('Start making groups dict')

	with open(input_group_path, 'r') as text_group_file:
		data = text_group_file.read()

	mcc_group_dict = {}
	mcc_dict = {}

	groups = data.split('\n\n')
	for group in groups:
		lines = group.split('\n')

		current_mccs = lines[1:]
		mcc_group_dict[lines[0]] = {}

		for mcc_line in current_mccs:
			mcc = int(mcc_line.split(':')[0])
			mcc_name = mcc_line.split(':')[1].strip().replace('\'', '')

			mcc_dict[mcc] = {'name': mcc_name, "group": lines[0]}
			mcc_group_dict[lines[0]][mcc] = mcc_name

	with open(output_group_path, 'w', encoding='UTF-8') as mcc_json:
		json.dump(mcc_group_dict, mcc_json, indent=4, ensure_ascii=False)
	logger.info(f"Saved mcc dictionary to {output_group_path}")

	with open(output_mcc_path, 'w', encoding='UTF-8') as group_json:
		json.dump(mcc_dict, group_json, indent=4, ensure_ascii=False)
	logger.info(f'Saved mcc groups dictionary to {output_mcc_path}')


if __name__ == '__main__':
	log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
	logging.basicConfig(level=logging.INFO, format=log_fmt)

	# project_dir = Path(__file__).resolve().parents[2]
	# load_dotenv(find_dotenv())

	main()
