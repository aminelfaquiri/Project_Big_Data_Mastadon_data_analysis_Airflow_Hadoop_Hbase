from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta
import subprocess
import sys
sys.path.insert(0, '/home/hadoop/MP/Mastodon_Data')
sys.path.insert(0, '/home/hadoop/MP/Hbase')
sys.path.insert(0, '/home/hadoop/MP/Mappreducers')
sys.path.insert(0, '/home/hadoop/MP/Analyse_Mastodon')

from get_data import get_data
from Tablecreator import Tablecreator
from Runer import Runer
from Analyse_Mastodon import Analyse_Mastodon


default_args = {
    'owner': 'admin',
    'start_date': datetime(2023, 10, 23),
    'retry_dely': timedelta(minutes=5)
}

with DAG('Mastodon_Workflow', default_args=default_args, schedule_interval=None) as dag:

    # get data from mastodon :
    def set_data_path(**kwargs):
        data_path = get_data()  # Run the data collection function
        processed_path = '/Mostodon/Raw/' + datetime.now().strftime('%Y-%m-%d/%H-%M') + '/'
        Variable.set("data_path", data_path)
        Variable.set("processed_path", processed_path)

    # Create PythonOperator tasks :
    retrieve_and_save_mastodon_data = PythonOperator(
        task_id='get_Data_Mastodon',
        provide_context=True,
        python_callable=set_data_path,
        dag=dag,
    )



    # task 2 : ?????????
    def create_tables_hbase(**kwargs):
        processed_path = Variable.get("processed_path")
        Runer(processed_path)

    create_tables_hbase_task = PythonOperator(
        task_id='run_create_tables',
        provide_context=True,
        python_callable=create_tables_hbase,
        dag=dag,  
    )

    # task 3 ??????:
    def run_map_reduce(**kwargs):
        data_path = Variable.get("data_path")  # Retrieve the data path from the variable
        output_path = Variable.get("processed_path")  # Retrieve the processed path from the variable
        # Use subprocess to run Hadoop MapReduce job with the provided data path
        hadoop_command = f"hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar " \
                          f"-mapper /home/project/Mastadon_data_analysis_Airflow_Hadoop_Hbase/mapReduce/python/mapper.py " \
                         f"-reducer /home/project/Mastadon_data_analysis_Airflow_Hadoop_Hbase/mapReduce/python/reducer.py " \
                         f"-input {data_path} " \
                          f"-output {output_path}"
        subprocess.run(hadoop_command, shell=True)


     run_map_reduce_task = PythonOperator(
         task_id='run map reduce',
         provide_context=True,
         python_callable=run_map_reduce,
         dag=dag,  
     )

     # task 4 : ??????
    def Analyse_Mastodon(**kwargs):
        processed_path = Variable.get("processed_path")
        Runer(processed_path)

    Analyse_Mastodon_task = PythonOperator(
        task_id='Analyse Mastodon',
        provide_context=True,
        python_callable=Analyse_Mastodon,
        dag=dag,  
    )


    retrieve_and_save_mastodon_data >> create_tables_hbase_task >> run_map_reduce_task >> Analyse_Mastodon_task

if __name__ == "__main__":
    dag.cli()

