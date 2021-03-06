# AAT Analysis
> This package helps with analyzing mobile AAT data.


## Install

`pip install aat_analysis`

## How to use

```python
#%run utils.ipynb # Some utility functions
#%run make_condition_templates.ipynb # Defines expected data based on resources
#%run json_to_df.ipynb # Turns raw json data into dataframes and calculates responses, rts, and force
```

```python
from aat_analysis.make_condition_templates import make_condition_templates
from aat_analysis.json_to_df import json_to_df
from aat_analysis.utils import merge_data

#from aat_analysis.
```

### Define folder paths
- raw should include the raw data from your experiment
- external should include the contents of the Resources folder of your experiment app
- interim and processed can be empty

```python
external_folder = "../data/external/"
interim_folder = "../data/interim/"
raw_data_folder = "../data/raw/"
processed_data_file = "../data/processed/data.csv"
```

### Preprocess data

```python
# Creates empty dataframes to define expected data for each condition
templates = make_condition_templates(external_folder)
# Preprocesses data for each participant and moves it to interim
json_to_df(raw_data_folder, external_folder, interim_folder, templates)
# Merges interim data and stores it for further analysis
data = merge_data(interim_folder, drop=['interpolated','interpolated_gyro'])
data.to_csv(processed_data_file)
```

    100%|█████████████████████████████████████████████| 3/3 [00:27<00:00,  9.24s/it]


### AAT data
The selected columns below contain all data needed to calculate approach tendencies for each session, participant, and stimulus type.  The additional data in the dataframe (not shown) are answers to other questions and some additional AAT variables.

```python
data[['participant','condition','session','trial','is_practice','stimulus_set','stimulus','correct_response','response','accuracy','rt','force']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>participant</th>
      <th>condition</th>
      <th>session</th>
      <th>trial</th>
      <th>is_practice</th>
      <th>stimulus_set</th>
      <th>stimulus</th>
      <th>correct_response</th>
      <th>response</th>
      <th>accuracy</th>
      <th>rt</th>
      <th>force</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>kmahu0zq</td>
      <td>condition_2</td>
      <td>final_session</td>
      <td>1</td>
      <td>False</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>NA</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kmahu0zq</td>
      <td>condition_2</td>
      <td>introduction_session_2</td>
      <td>1</td>
      <td>True</td>
      <td>practice_food</td>
      <td>stim_0154</td>
      <td>push</td>
      <td>ND</td>
      <td>False</td>
      <td>NaN</td>
      <td>8.124186</td>
    </tr>
    <tr>
      <th>2</th>
      <td>kmahu0zq</td>
      <td>condition_2</td>
      <td>introduction_session_2</td>
      <td>2</td>
      <td>True</td>
      <td>practice_objects</td>
      <td>stim_1276</td>
      <td>pull</td>
      <td>pull</td>
      <td>True</td>
      <td>1206.0</td>
      <td>12.130466</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kmahu0zq</td>
      <td>condition_2</td>
      <td>introduction_session_2</td>
      <td>3</td>
      <td>True</td>
      <td>practice_objects</td>
      <td>stim_1264</td>
      <td>pull</td>
      <td>ND</td>
      <td>False</td>
      <td>NaN</td>
      <td>1.651279</td>
    </tr>
    <tr>
      <th>4</th>
      <td>kmahu0zq</td>
      <td>condition_2</td>
      <td>introduction_session_2</td>
      <td>4</td>
      <td>True</td>
      <td>practice_objects</td>
      <td>stim_1277</td>
      <td>pull</td>
      <td>pull</td>
      <td>True</td>
      <td>629.0</td>
      <td>18.342323</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6166</th>
      <td>kmah8va6</td>
      <td>condition_2</td>
      <td>push_food_before_lunch_d5</td>
      <td>132</td>
      <td>False</td>
      <td>unhealthy_tempting</td>
      <td>stim_0025</td>
      <td>pull</td>
      <td>pull</td>
      <td>True</td>
      <td>346.0</td>
      <td>9.024626</td>
    </tr>
    <tr>
      <th>6167</th>
      <td>kmah8va6</td>
      <td>condition_2</td>
      <td>push_food_before_lunch_d5</td>
      <td>133</td>
      <td>False</td>
      <td>unhealthy_non_tempting</td>
      <td>stim_0125</td>
      <td>pull</td>
      <td>pull</td>
      <td>True</td>
      <td>363.0</td>
      <td>5.820239</td>
    </tr>
    <tr>
      <th>6168</th>
      <td>kmah8va6</td>
      <td>condition_2</td>
      <td>push_food_before_lunch_d5</td>
      <td>134</td>
      <td>False</td>
      <td>healthy_non_tempting</td>
      <td>stim_0226</td>
      <td>pull</td>
      <td>pull</td>
      <td>True</td>
      <td>492.0</td>
      <td>8.345508</td>
    </tr>
    <tr>
      <th>6169</th>
      <td>kmah8va6</td>
      <td>condition_2</td>
      <td>push_food_before_lunch_d5</td>
      <td>135</td>
      <td>False</td>
      <td>healthy_tempting</td>
      <td>stim_0201</td>
      <td>pull</td>
      <td>pull</td>
      <td>True</td>
      <td>450.0</td>
      <td>5.539470</td>
    </tr>
    <tr>
      <th>6170</th>
      <td>kmah8va6</td>
      <td>condition_2</td>
      <td>push_food_before_lunch_d5</td>
      <td>136</td>
      <td>False</td>
      <td>objects</td>
      <td>stim_1035</td>
      <td>push</td>
      <td>pull</td>
      <td>False</td>
      <td>308.0</td>
      <td>6.589124</td>
    </tr>
  </tbody>
</table>
<p>6171 rows × 12 columns</p>
</div>


