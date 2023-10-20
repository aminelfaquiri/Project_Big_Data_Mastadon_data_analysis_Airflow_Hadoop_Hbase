# Project Big Data Mastodon Data Analysis with Airflow, Hadoop, and HBase

## Introduction

This project is dedicated to the analysis of data from the Mastodon platform and aims to address various critical needs for the extraction, processing, and analysis of massive data. As a data developer, the mission is to establish an automated pipeline to tackle these complex challenges. This project responds to the necessity of extracting meaningful insights from raw Mastodon data, focusing on user analysis, content analysis, language analysis, media engagement, tags, mentions, and more. To achieve this, several key steps need to be followed, from raw data collection to in-depth analysis of the results. These needs define the framework of this Big Data project and will be detailed in the following sections.

## Planning

### Requirements Expression

- **Data Collection:** Use the Mastodon API, store data in HDFS, and model the HDFS Data Lake.
- **MapReduce Processing:** Mapper and reducer to transform and aggregate data.
- **MapReduce Job Execution:** Utilize the Hadoop streaming API and monitor through the Hadoop Web interface.
- **Store Results in HBase:** Design the HBase schema, create tables, and insert data.
- **Orchestration with Apache Airflow:** Define a DAG, create tasks, and monitor through Airflow.
- **Results Analysis:** Query data in HBase to extract information about users, content, language, media engagement, tags, and mentions.
- **Optimization and Monitoring:** Optimize MapReduce scripts, monitor HBase, set up Airflow alerts, and monitor Hadoop.
- **Update Permissions and Documentation:** Update API tokens, document roles, permissions, and access rules.
- **Scheduled Developments:** Regularly schedule DAGs to keep data current.
- **GDPR Compliance:** Document personal data, comply with GDPR regulations.

### Environment Preparation

#### Install Hadoop

#### HBase Installation

1. **Download HBase**:

   ```bash
   wget http://www.interior-dsgn.com/apache/hbase/stable/hbase-2.5.5-bin.tar.gz
