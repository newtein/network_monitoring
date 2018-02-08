import matplotlib.pyplot as plt 
import numpy as np
import pickle
from collections import OrderedDict

import matplotlib.pyplot as plt 
import numpy as np
plt.close()
import seaborn as sns
import datetime
sns.set()

# plt.style.use('ggplot')
# plt.rcParams['axes.facecolor']='white'
# plt.rcParams['grid.color']='gainsboro'

fig, ax = plt.subplots(dpi=300)
fig.set_size_inches(11, 4.3)

data=pickle.load(open("tempdata","rb"))

#data=OrderedDict([('172.16.99.204', [(1491656192.17, 1), (1491656192.89, 2), (1491656193.43, 2), (1491656193.69, 2), (1491656194.26, 1), (1491656197.7, 1), (1491656199.09, 2), (1491656199.59, 2), (1491673585.16, 1), (1491673585.16, 1), (1491673585.18, 1), (1491673585.19, 1), (1491673585.35, 2), (1491673585.5, 1), (1491673585.53, 1), (1491673585.66, 1), (1491673585.83, 1), (1491673585.86, 2), (1491673586.0, 1), (1491673586.18, 2), (1491673586.2, 1), (1491673586.35, 1), (1491673586.78, 2), (1491673586.97, 2), (1491673587.14, 2), (1491673587.31, 1), (1491673587.47, 1), (1491673587.65, 1), (1491673587.82, 1), (1491673587.98, 1), (1491673588.19, 2), (1491673588.31, 2), (1491673588.36, 2), (1491673588.43, 1), (1491673588.53, 1), (1491673588.56, 1), (1491673588.73, 1), (1491673588.9, 1), (1491673589.06, 1), (1491673589.1, 1), (1491673589.23, 1), (1491673589.43, 1), (1491673589.59, 2), (1491673589.79, 1), (1491673589.99, 1), (1491673590.16, 1), (1491673590.33, 1), (1491673590.51, 2), (1491673590.69, 2), (1491673590.88, 1), (1491673591.06, 1), (1491673591.23, 1), (1491673591.4, 1), (1491673591.57, 1), (1491673591.75, 1), (1491673591.92, 1), (1491673592.1, 2), (1491673592.27, 1), (1491673592.45, 1), (1491673592.62, 1), (1491673592.78, 1), (1491673592.97, 1), (1491673593.14, 2), (1491673593.36, 2), (1491673593.71, 1), (1491673593.88, 1), (1491673594.06, 1), (1491673594.23, 1), (1491673594.4, 2), (1491673594.56, 2), (1491673594.73, 1), (1491673594.9, 1), (1491673595.07, 1), (1491673595.27, 1), (1491673595.44, 2), (1491673595.61, 1), (1491673595.78, 2), (1491673595.95, 1), (1491673596.14, 1), (1491673596.33, 1), (1491673596.51, 1), (1491673596.68, 2), (1491673596.84, 2), (1491673597.01, 2), (1491673597.17, 1), (1491673597.37, 1), (1491673597.73, 1), (1491673597.9, 2), (1491673598.07, 2), (1491673598.24, 2), (1491673598.41, 1), (1491673598.57, 1), (1491673598.75, 1), (1491673598.92, 1), (1491673599.09, 1), (1491673599.26, 2), (1491673599.43, 2), (1491673599.6, 1), (1491673599.76, 1), (1491673599.93, 1), (1491673600.09, 1), (1491673600.26, 2), (1491673600.42, 1), (1491673600.59, 2), (1491673600.75, 1), (1491673600.93, 1), (1491673601.11, 1), (1491673604.0, 1), (1491673642.5, 2), (1491673647.85, 2), (1491673649.04, 2), (1491673650.28, 2), (1491660777.21, 2), (1491661129.77, 1), (1491661130.54, 2), (1491664377.29, 2), (1491667977.27, 2), (1491670308.26, 1), (1491670308.72, 1), (1491670309.23, 1), (1491670309.23, 2), (1491670309.23, 1), (1491670309.98, 2), (1491670309.98, 2), (1491670310.86, 2), (1491670311.04, 1), (1491670311.04, 1), (1491670311.05, 1), (1491670311.2, 1), (1491670311.25, 2), (1491670311.26, 2), (1491670311.47, 1), (1491670311.47, 1), (1491670311.49, 1), (1491670314.83, 2), (1491670315.0, 2), (1491670315.0, 2), (1491670320.19, 1), (1491670325.28, 2)]), ('172.16.98.86', [(1491656403.53, 2), (1491656482.14, 2), (1491656482.67, 2), (1491656484.76, 2), (1491656484.76, 2), (1491656484.76, 2), (1491656485.37, 2), (1491656485.37, 2), (1491656486.2, 2), (1491656486.2, 2), (1491656486.2, 2), (1491656486.2, 2), (1491656498.42, 2), (1491656498.42, 2), (1491656498.42, 2), (1491656498.42, 2), (1491656498.42, 2), (1491656498.42, 2), (1491656498.46, 2), (1491656498.91, 2), (1491656498.97, 2), (1491656499.04, 2), (1491656499.38, 2), (1491656499.38, 2), (1491656500.19, 2), (1491656500.41, 2), (1491656500.95, 2), (1491656501.49, 2), (1491656501.49, 2), (1491656505.45, 2), (1491656505.45, 2), (1491656505.45, 2), (1491656505.45, 2), (1491656505.45, 2), (1491656506.04, 2), (1491656506.04, 2), (1491656506.04, 2), (1491656506.84, 2), (1491656510.48, 2), (1491656511.15, 2), (1491656511.15, 2), (1491656511.15, 2), (1491656511.16, 2), (1491656512.74, 2), (1491656513.43, 2), (1491656524.81, 2), (1491656526.35, 2), (1491656542.74, 2), (1491656542.74, 2), (1491656542.74, 2), (1491656542.74, 2), (1491656542.9, 2), (1491656543.15, 2), (1491656543.15, 2), (1491656572.15, 2), (1491656572.66, 2), (1491656588.53, 2), (1491656588.67, 2), (1491656589.43, 2), (1491656589.61, 2), (1491656590.53, 2), (1491656591.54, 2), (1491656591.54, 2), (1491656591.65, 2), (1491656591.66, 2), (1491656591.86, 2), (1491656591.86, 2), (1491656591.86, 2), (1491656591.86, 2), (1491656592.11, 2), (1491656592.38, 2), (1491656592.52, 2), (1491656592.97, 2), (1491656593.31, 2), (1491656594.11, 2), (1491656594.2, 2), (1491656594.24, 2), (1491656594.32, 2), (1491656594.87, 2), (1491656603.65, 2), (1491656604.91, 2), (1491656605.48, 2), (1491656616.83, 2), (1491656617.0, 2), (1491656617.0, 2), (1491656617.0, 2), (1491656617.0, 2), (1491656617.0, 2), (1491656617.0, 2), (1491656617.89, 2), (1491656619.01, 2), (1491656619.01, 2), (1491656619.01, 2), (1491656619.12, 2), (1491656619.27, 2), (1491656620.04, 2), (1491656620.12, 2), (1491656620.56, 2), (1491656620.56, 2), (1491656620.66, 2), (1491656621.38, 2), (1491656621.87, 2), (1491656622.42, 2), (1491656622.91, 2), (1491656623.43, 2), (1491656623.96, 2), (1491656624.05, 2), (1491673265.36, 2), (1491658354.23, 2), (1491658513.85, 2), (1491658513.87, 2), (1491658753.59, 2), (1491658753.62, 2), (1491658990.66, 2), (1491658990.66, 2), (1491658990.66, 2), (1491658990.68, 2), (1491659054.33, 2), (1491659114.53, 2), (1491659350.53, 2), (1491659350.55, 2), (1491659593.59, 2), (1491659593.6, 2), (1491659593.83, 2), (1491659593.84, 2), (1491659594.26, 2), (1491659594.26, 2), (1491659595.1, 2), (1491659596.77, 2), (1491659600.14, 2), (1491659606.86, 2), (1491659620.35, 2), (1491659647.27, 2), (1491659647.27, 2), (1491659647.27, 2), (1491659647.27, 2), (1491659953.72, 2), (1491659980.4, 2), (1491659980.4, 2), (1491659980.41, 2), (1491659980.41, 2), (1491659980.41, 2), (1491659980.41, 2), (1491659980.42, 2), (1491660174.03, 1), (1491660174.03, 1), (1491660174.04, 1), (1491660174.04, 2), (1491660190.59, 2), (1491660190.6, 2), (1491660430.59, 2), (1491660430.59, 2), (1491660430.59, 2), (1491660430.59, 2), (1491660430.63, 2), (1491660430.63, 2), (1491660430.63, 2), (1491660529.56, 2), (1491660563.03, 2), (1491660563.04, 1), (1491660563.09, 2), (1491660563.12, 1), (1491660563.14, 2), (1491660563.38, 2), (1491660563.43, 1), (1491661030.54, 2), (1491661030.54, 2), (1491661030.54, 2), (1491661030.54, 2), (1491661078.48, 2), (1491661393.47, 2), (1491661489.08, 2), (1491662233.37, 2), (1491662364.01, 2), (1491662470.43, 2), (1491662589.5, 2), (1491662833.82, 2), (1491662834.28, 2), (1491663410.41, 2), (1491663593.55, 2), (1491663593.97, 2), (1491663594.81, 2), (1491663596.49, 2), (1491663599.84, 2), (1491663606.59, 2), (1491663620.07, 2), (1491663646.99, 2), (1491663793.53, 2), (1491663793.55, 2), (1491664150.33, 2), (1491664390.34, 2), (1491664390.34, 2), (1491664390.34, 2), (1491664390.35, 2), (1491664391.84, 2), (1491664393.52, 2), (1491664393.52, 2), (1491664393.52, 2), (1491664393.52, 2), (1491664393.52, 2), (1491664444.06, 2), (1491664633.3, 2), (1491664633.32, 2), (1491665073.17, 2), (1491665073.17, 1), (1491665073.24, 2), (1491665073.24, 1), (1491665073.27, 2), (1491665073.28, 1), (1491665133.53, 2), (1491665133.53, 2), (1491665133.53, 2), (1491665133.53, 2), (1491665133.53, 2), (1491665145.69, 2), (1491665180.5, 2), (1491665180.5, 2), (1491665180.5, 2), (1491665180.5, 2), (1491669414.62, 2), (1491669414.69, 2), (1491669414.69, 2), (1491669414.69, 2), (1491669414.69, 2), (1491669414.69, 2), (1491669414.69, 2), (1491669414.74, 2), (1491669414.85, 2), (1491669414.85, 2), (1491669414.85, 2), (1491669419.73, 2), (1491669419.73, 2), (1491669419.85, 2), (1491669419.85, 2), (1491669419.85, 2), (1491669419.85, 2), (1491669419.85, 2), (1491669419.85, 2), (1491669419.86, 2), (1491669442.7, 2), (1491669443.73, 2), (1491669443.85, 2), (1491669443.85, 2), (1491669443.85, 2), (1491669443.85, 2), (1491669443.85, 2), (1491669443.85, 2), (1491669443.85, 2), (1491669444.33, 2), (1491669444.42, 2), (1491669444.42, 2), (1491669444.42, 2), (1491669444.42, 2), (1491669444.51, 2), (1491669444.51, 2), (1491669444.51, 2), (1491669444.98, 2), (1491669444.98, 2), (1491669444.98, 2), (1491669444.98, 2), (1491669444.98, 2), (1491669444.98, 2), (1491669445.11, 2), (1491669445.11, 2), (1491669445.11, 2), (1491669445.11, 2), (1491669445.11, 2), (1491669446.56, 2), (1491669446.56, 2), (1491669446.68, 2), (1491669447.0, 2), (1491669447.08, 2), (1491669448.06, 2), (1491669539.9, 2), (1491669556.68, 2), (1491669556.68, 2), (1491669556.68, 2), (1491669556.68, 2), (1491669556.68, 2), (1491669556.68, 2), (1491669556.68, 2), (1491669556.68, 2), (1491669556.68, 2), (1491669556.68, 2), (1491669558.93, 2), (1491669558.93, 2), (1491669558.93, 2), (1491669558.93, 2), (1491669559.06, 2), (1491669559.06, 2), (1491669559.06, 2), (1491669559.06, 2), (1491669559.06, 2), (1491669559.06, 2), (1491669559.47, 2), (1491669563.54, 2), (1491669564.25, 2), (1491669571.55, 2), (1491669571.55, 2), (1491669571.55, 2), (1491669571.55, 2), (1491669571.56, 2), (1491669571.56, 2), (1491669631.69, 2), (1491669631.69, 2), (1491669631.69, 2), (1491669631.69, 2), (1491669632.33, 2), (1491669632.88, 2), (1491669633.71, 2), (1491669634.35, 2), (1491669634.96, 2), (1491669635.02, 2), (1491669635.11, 2), (1491669635.82, 2), (1491669635.89, 2), (1491669636.57, 2), (1491669637.49, 2), (1491669637.59, 2), (1491669637.67, 2), (1491669637.67, 2), (1491669637.67, 2), (1491669637.67, 2), (1491669637.74, 2), (1491669638.87, 2), (1491669640.46, 2), (1491669640.46, 2), (1491669640.46, 2), (1491669641.19, 2), (1491669641.19, 2), (1491669641.19, 2), (1491669641.19, 2), (1491669642.05, 2), (1491669642.12, 2), (1491669642.18, 2), (1491669642.24, 2), (1491669642.31, 2), (1491669654.21, 2), (1491669655.0, 2), (1491669655.08, 2), (1491669655.93, 2), (1491669655.99, 2), (1491669655.99, 2), (1491669655.99, 2), (1491669656.06, 2), (1491669657.53, 2), (1491669658.29, 2), (1491670096.89, 2), (1491670097.68, 2), (1491670098.15, 2), (1491670113.11, 2), (1491670114.01, 2), (1491670114.54, 2), (1491670114.61, 2), (1491670115.16, 2), (1491670115.23, 2), (1491670115.23, 2), (1491670115.3, 2), (1491670115.42, 2), (1491670116.79, 2), (1491670118.01, 2), (1491670118.59, 2), (1491670131.42, 2), (1491670131.88, 2), (1491670132.57, 2), (1491670140.83, 2), (1491670198.21, 2), (1491670198.31, 2), (1491670198.31, 2), (1491670198.61, 2), (1491670198.61, 2), (1491670198.67, 2), (1491670198.75, 2), (1491670198.75, 2), (1491670198.75, 2), (1491670198.93, 1), (1491670198.93, 1), (1491670198.93, 1), (1491670198.93, 1), (1491670198.93, 1), (1491670198.93, 1), (1491670198.94, 1), (1491670199.05, 2), (1491670199.05, 2), (1491670199.73, 2), (1491670200.63, 2), (1491670200.63, 2), (1491670200.63, 2), (1491670200.9, 2), (1491670200.9, 2), (1491670200.9, 2), (1491670200.9, 2), (1491670200.9, 2), (1491670201.95, 2), (1491670202.18, 2), (1491670203.61, 2)]), ('172.16.100.81', [(1491656484.8, 2), (1491656487.05, 2), (1491656580.22, 1), (1491656580.42, 1), (1491656602.73, 2), (1491656626.13, 2), (1491656628.21, 2), (1491656629.46, 2), (1491656634.69, 2), (1491656635.69, 2), (1491656636.75, 2), (1491656637.47, 1), (1491656638.52, 1), (1491657926.32, 2), (1491657927.08, 2), (1491657932.59, 2), (1491657933.85, 2), (1491658665.24, 2), (1491658665.24, 1), (1491658665.37, 2), (1491658665.44, 2), (1491658665.55, 1), (1491668239.62, 2), (1491668251.41, 2), (1491668251.41, 1), (1491668251.41, 1), (1491668251.54, 2), (1491668251.54, 2), (1491668251.54, 2), (1491668251.6, 1), (1491668251.75, 2), (1491668251.75, 2), (1491668251.99, 2), (1491668252.05, 2), (1491668252.06, 2), (1491668252.16, 1), (1491668252.25, 2), (1491668257.01, 1), (1491668261.34, 1), (1491668265.38, 1), (1491668266.05, 1), (1491668269.15, 1), (1491668271.12, 2), (1491668273.23, 2), (1491668382.38, 2), (1491668568.15, 2), (1491668733.11, 2), (1491668784.56, 2), (1491668797.31, 2), (1491668798.25, 2), (1491668798.25, 2), (1491668798.25, 1), (1491668798.25, 2), (1491668883.06, 2), (1491668930.95, 2), (1491669173.02, 1), (1491669173.44, 2), (1491669406.14, 2), (1491669570.55, 2), (1491669650.95, 2), (1491669683.85, 2), (1491669701.85, 1), (1491669720.54, 2), (1491671656.3, 2), (1491671656.33, 2), (1491671656.33, 1), (1491671656.33, 1), (1491671656.33, 1), (1491671656.33, 1), (1491671656.33, 1), (1491671656.33, 1), (1491671656.43, 2), (1491671656.49, 2), (1491671656.49, 2), (1491671656.96, 2), (1491671656.97, 2), (1491671657.5, 2), (1491671657.59, 2), (1491671657.6, 2), (1491671681.25, 2), (1491671683.61, 2), (1491671696.51, 2), (1491671716.49, 2), (1491671834.47, 2), (1491671972.44, 2), (1491672036.88, 1), (1491672092.17, 2), (1491672416.54, 2), (1491672416.54, 2), (1491672416.54, 1), (1491672416.54, 1), (1491672568.42, 2), (1491672647.82, 2), (1491672732.43, 1), (1491672732.47, 2)]), ('10.18.118.136', [(1491656573.55, 2), (1491656573.55, 2), (1491656573.55, 2), (1491656573.82, 2), (1491656573.82, 2), (1491656573.82, 2), (1491656574.08, 2), (1491656574.89, 2), (1491656575.16, 2), (1491656576.18, 2), (1491656576.84, 2), (1491656578.38, 2), (1491656578.65, 2), (1491656578.93, 2), (1491656579.49, 2), (1491656580.61, 2), (1491656580.61, 2), (1491656580.61, 2), (1491656580.61, 2), (1491656582.85, 2), (1491656582.85, 2), (1491656582.85, 2), (1491656582.85, 2), (1491656582.85, 2), (1491656587.36, 2), (1491656587.36, 2), (1491656596.33, 2), (1491656614.29, 2)]), ('172.16.101.151', [(1491663662.46, 2)]), ('172.16.101.236', [(1491660666.46, 2)]), ('172.16.104.242', [(1491661858.91, 1), (1491661867.11, 2), (1491661905.53, 1), (1491661905.54, 1), (1491661905.54, 1), (1491661905.54, 1), (1491661905.58, 1), (1491661905.59, 1), (1491661905.59, 1), (1491661905.59, 1), (1491661905.61, 1), (1491661905.61, 1), (1491661905.61, 1), (1491661905.61, 1), (1491661905.61, 1), (1491661905.62, 1), (1491661905.62, 1), (1491661905.63, 1), (1491661905.63, 1), (1491661905.63, 1), (1491661905.64, 1), (1491661905.66, 1), (1491661905.66, 1), (1491661905.67, 1), (1491661905.9, 1), (1491661905.9, 1), (1491661905.93, 1), (1491661905.93, 1), (1491661905.93, 1), (1491661905.93, 1), (1491661905.93, 1), (1491661905.93, 1), (1491661905.93, 1), (1491661905.93, 1), (1491661905.94, 1), (1491661905.95, 1), (1491661905.95, 1), (1491661905.96, 1), (1491661936.05, 1), (1491661936.05, 1), (1491661936.05, 1), (1491661936.06, 1), (1491661936.06, 1), (1491661962.78, 1), (1491661962.78, 1), (1491661986.98, 2), (1491662076.99, 2), (1491662155.74, 1), (1491662155.74, 1), (1491662185.83, 1), (1491662196.97, 2), (1491662347.02, 2), (1491662406.21, 1), (1491662436.49, 1), (1491662587.0, 2), (1491662647.04, 2), (1491662647.25, 1), (1491662647.25, 1), (1491662647.25, 1), (1491662647.25, 1), (1491662647.25, 1), (1491662647.25, 1), (1491662647.25, 1), (1491662647.26, 1), (1491662647.31, 1), (1491662647.33, 1), (1491662647.33, 1), (1491662647.33, 1), (1491662647.35, 1), (1491662647.36, 1), (1491662647.37, 1), (1491662647.38, 1), (1491662647.94, 1), (1491662647.95, 1), (1491662647.95, 1), (1491662647.96, 1), (1491662647.99, 1), (1491662647.99, 1), (1491662647.99, 1), (1491662648.01, 1), (1491662648.02, 1), (1491662648.02, 1), (1491662648.04, 1), (1491662648.04, 1), (1491662648.04, 1), (1491662648.04, 1), (1491662648.05, 1), (1491662648.06, 1), (1491662648.07, 1), (1491662677.51, 1), (1491662677.51, 1), (1491662677.52, 1), (1491662677.52, 1), (1491662677.53, 1), (1491662677.54, 1), (1491662677.6, 1), (1491662677.6, 1), (1491662677.6, 1), (1491662677.6, 1), (1491662677.6, 1), (1491662678.14, 1), (1491662678.14, 1), (1491662678.14, 1), (1491662678.17, 1), (1491662678.25, 1), (1491662706.96, 2), (1491663164.65, 2), (1491663352.48, 1), (1491663450.81, 2), (1491663510.81, 2), (1491663570.82, 2), (1491663593.55, 1), (1491663623.21, 1), (1491663864.4, 1), (1491663864.4, 1), (1491663864.4, 1), (1491663864.4, 1), (1491663864.49, 1), (1491663864.5, 1), (1491663864.5, 1), (1491663864.5, 1), (1491663864.5, 1), (1491663864.5, 1), (1491663864.5, 1), (1491663864.52, 1), (1491663864.52, 1), (1491663864.53, 1), (1491663864.54, 1), (1491663864.54, 1), (1491663864.92, 1), (1491663864.92, 1), (1491663864.92, 1), (1491663864.92, 1), (1491663864.92, 1), (1491663864.92, 1), (1491663864.93, 1), (1491663864.93, 1), (1491663864.94, 1), (1491663864.94, 1), (1491663864.94, 1), (1491663864.94, 1), (1491663864.95, 1), (1491663864.95, 1), (1491663864.96, 1), (1491663864.96, 1), (1491663864.97, 1), (1491663864.98, 1), (1491664075.67, 1), (1491664076.3, 1), (1491664316.73, 1), (1491664316.73, 1), (1491664316.73, 1), (1491664316.73, 1), (1491664317.57, 1), (1491664317.57, 1), (1491664557.95, 1), (1491664557.97, 1), (1491664558.02, 1), (1491664558.04, 1), (1491664558.04, 1), (1491664558.07, 1), (1491664558.32, 1), (1491664558.32, 1), (1491664558.33, 1), (1491664558.33, 1), (1491664558.33, 1), (1491664558.34, 1), (1491664558.35, 1), (1491664558.35, 1), (1491664558.36, 1), (1491664558.36, 1), (1491664558.37, 1), (1491664558.37, 1), (1491664558.38, 1), (1491664558.39, 1), (1491664558.39, 1), (1491664558.43, 1), (1491664558.44, 1), (1491664558.45, 1), (1491664799.27, 1), (1491664829.36, 1), (1491665040.17, 1), (1491665040.17, 1), (1491665040.17, 1), (1491665040.17, 1), (1491665040.25, 1), (1491665040.27, 1), (1491665040.27, 1), (1491665040.3, 1), (1491665040.31, 1), (1491665040.59, 1), (1491665040.59, 1), (1491665040.6, 1), (1491665040.64, 1), (1491665040.64, 1), (1491665040.66, 1), (1491665291.0, 1), (1491665320.66, 1), (1491665531.71, 1), (1491665531.71, 1), (1491665531.71, 1), (1491665531.72, 1), (1491665531.76, 1), (1491665531.76, 1), (1491665531.77, 1), (1491665531.8, 1), (1491665531.8, 1), (1491665531.8, 1), (1491665531.81, 1), (1491665531.82, 1), (1491665531.83, 1), (1491665531.84, 1), (1491665531.85, 1), (1491665532.26, 1), (1491665532.27, 1), (1491665532.28, 1), (1491665532.28, 1), (1491665532.28, 1), (1491665532.29, 1), (1491665532.3, 1), (1491665532.33, 1), (1491665532.33, 1), (1491665532.33, 1), (1491665532.33, 1), (1491665532.33, 1), (1491665561.93, 1), (1491665773.02, 1), (1491665773.02, 1), (1491665773.02, 1), (1491665773.02, 1), (1491665773.02, 1), (1491665773.02, 1), (1491665773.02, 1), (1491665773.02, 1), (1491665773.02, 1), (1491665773.02, 1), (1491665773.02, 1), (1491665773.02, 1), (1491665773.09, 1), (1491665773.1, 1), (1491665773.11, 1), (1491665773.11, 1), (1491665773.14, 1), (1491665773.14, 1), (1491665773.14, 1), (1491665773.14, 1), (1491665773.14, 1), (1491665773.56, 1), (1491665773.56, 1), (1491665773.57, 1), (1491665773.57, 1), (1491665773.58, 1), (1491665773.58, 1), (1491665773.59, 1), (1491665773.59, 1), (1491665773.62, 1), (1491665773.62, 1), (1491665773.62, 1), (1491665773.62, 1), (1491665773.63, 1), (1491665802.74, 1), (1491665802.74, 1), (1491665802.75, 1), (1491665802.75, 1), (1491665802.79, 1), (1491665802.79, 1), (1491665802.8, 1), (1491665802.81, 1), (1491665802.81, 1), (1491665802.82, 1), (1491665802.82, 1), (1491665802.83, 1), (1491665802.83, 1), (1491665802.84, 1), (1491665802.85, 1), (1491665803.1, 1), (1491665803.1, 1), (1491665803.11, 1), (1491665803.12, 1), (1491665803.13, 1), (1491665803.13, 1), (1491665803.13, 1), (1491665803.15, 1), (1491665803.15, 1), (1491665803.16, 1), (1491665862.98, 2), (1491665862.99, 2), (1491665862.99, 2), (1491665863.01, 2)]), ('172.16.103.217', [(1491662333.3, 1), (1491662342.95, 2), (1491662372.16, 2), (1491662570.5, 2), (1491662570.59, 2), (1491662570.81, 2), (1491662570.84, 2), (1491662601.98, 1), (1491663159.88, 1), (1491663165.38, 1), (1491663170.78, 2), (1491663170.79, 1)]), ('172.16.102.59', [(1491665961.16, 1)]), ('10.89.248.52', [(1491669643.56, 2), (1491669644.19, 2), (1491669644.47, 2), (1491669645.07, 2), (1491669645.07, 2), (1491669645.07, 2), (1491669645.07, 2), (1491669645.65, 2), (1491669645.65, 2), (1491669645.65, 2), (1491669645.65, 2), (1491669645.65, 2), (1491669646.81, 2), (1491669649.13, 2), (1491669649.13, 2), (1491669649.13, 2), (1491669649.13, 2), (1491669649.13, 2), (1491669653.78, 2), (1491669663.07, 2), (1491669663.07, 2), (1491669681.68, 2), (1491669718.82, 2), (1491670205.11, 2)])])

# Create egress score file

x,y=[],[]

ndata={}
for ips in data:
	ndata[ips]=OrderedDict()
	for i in range(len(data[ips])):
		data[ips][i]=list(data[ips][i])
		data[ips][i][0]=int(data[ips][i][0])
		if data[ips][i][0] not in ndata[ips]:
			ndata[ips][data[ips][i][0]]=[]
		ndata[ips][data[ips][i][0]].append(data[ips][i][1])
for ips in ndata:
	for timestamp in ndata[ips]:
		ndata[ips][timestamp]=np.mean([i for i in ndata[ips][timestamp]])



# f=open("egress_score","w")
# for ipv4 in ndata:
# 	for timestamp in ndata[ipv4]:
# 		f.write(ipv4+","+str(ndata[ipv4][timestamp])+","+str(timestamp)+"\n")	
# f.close()

# ends
def cal_theeta(fname):

	
	data={}
	f=open(fname,"r")
	next(f)
	for l in f:
		row=l.split(",")
		row[1:]=[float(i.strip()) for i in row[1:]]
		key=row[0].replace("'","")
		if key not in data:
			data[key]=OrderedDict()
		

		ts=float(row[-1])
		#print(data,ts)
		
		data[key][ts]=1
		
	return data


def cal_gamma(fname):

	weight=1.0
	data={}
	f=open(fname,"r")
	next(f)
	for l in f:
		row=l.split(",")
		row[1:]=[float(i.strip()) for i in row[1:]]
		key=row[0].replace("'","")
		if key not in data:
			data[key]=OrderedDict()
		

		ts=int(row[-1])
		#print(data,ts)
		
		data[key][ts]=(weight* row[1]) + (weight*row[2])
		
	return data

def cal_beta(fname):

	# beta = 4 * (type b + type a.b) + 1 * (type a + type (a+b))
	wa=4.0/5.0
	wb=1.0/5.0
	data={}
	f=open(fname,"r")
	next(f)
	for l in f:
		row=l.split(",")
		row[1:5]=[float(i.strip()) for i in row[1:5]]
		key=row[0].replace("'","")
		if key not in data:
			data[key]=OrderedDict()
		try:

			ts=float(row[-1])
			#print(data,ts)
			
			data[key][ts]=(wa* (row[1]+ row[3])) + (wb*(row[2]+row[4]))
		except:
			pass
	return data

def cal_alpha(ndata):
	# alpha=4*illicit + 1 * suspected
	wa=4.0/5.0
	wb=1.0/5.0

	for ipv4 in ndata:
		for ts in ndata[ipv4]:
			if (ndata[ipv4][ts]==2):
				ndata[ipv4][ts]=ndata[ipv4][ts]*wa
			elif (ndata[ipv4][ts]==1):
				ndata[ipv4][ts]=ndata[ipv4][ts]*wb
	return ndata


def warning(tplot,wflag,risk):
	for i in tplot:
		if wflag<3:
			if tplot[i]<0.25:
				pass
			else:
				wflag+=1
				ax.scatter(i-2,0.25,color='k',s=10)
				
				print(63+wflag)
				if risk=="HIGH" or risk=="CRITICAL":
					wflag=3
					print(ips,"Risk HIGH/C")
				print("??",ips,tplot[i],i)

		if wflag==3:
			print("Blocked: ",ips,tplot[i],i)
			wflag+=1
			
		elif wflag>3:
			del tplot[i]
	return tplot,wflag




files=["egress_score.csv","vds_score.csv","scan_score.csv","fingerprint_score.csv"]

alpha=cal_alpha(ndata)
beta=cal_beta(files[1])
gamma=cal_gamma(files[3])
theeta=cal_theeta(files[2])
print(gamma)

ndata=alpha
fool=0
tt=list(set(alpha.keys()+beta.keys()+gamma.keys()+theeta.keys()))
iplist=['172.16.99.204','172.16.68.31','172.16.98.86','172.16.105.59','172.16.102.59','172.16.248.52']
for ips in iplist:
	wflag=0
	
	tperiod=1
	aminx=min(ndata.get(ips,{0:0}).keys())
	amaxx=max(ndata.get(ips,{0:0}).keys())

	bminx=min(beta.get(ips,{0:0}).keys())
	bmaxx=max(beta.get(ips,{0:0}).keys())
		
	gminx=min(gamma.get(ips,{0:0}).keys())
	gmaxx=max(gamma.get(ips,{0:0}).keys())

	tminx=min(theeta.get(ips,{0:0}).keys())
	tmaxx=max(theeta.get(ips,{0:0}).keys())
	
	tmax=[amaxx , bmaxx , gmaxx , tmaxx]
	tmin=[aminx , bminx , gminx , tminx]
	tmin=filter(lambda a:a!=0, tmin)
	tmax.sort()
	tmin.sort()
	maxx=int(tmax[-1])+100
	minx=int(tmin[0])

	timedelta=maxx-minx
	tplot=OrderedDict()
	fool1=0
	while(minx<maxx):
		ttx=[]
		tty=[]
		tperiod=1 
		for i in range(minx,minx+tperiod):
			#print(i)
			b=beta.get(ips,0)			
			g=gamma.get(ips,0)


			the=theeta.get(ips,0)
			a=ndata.get(ips,0)	
		
			if b!=0:
				b=beta[ips].get(i,0)
			if g!=0:
				g=gamma[ips].get(i,0)
				if g!=0:
					print(g,i,ips)
			if the!=0:
				the=theeta[ips].get(i,0)
			if a!=0:
				a=ndata[ips].get(i,0)
			
			terminal_score=(a+b+(2.0*g)+2.0*the)/6.0

			if ips=='172.16.98.86' and (g!=0 or b!=0 or a!=0 or the!=0):
				#print(ips,a,b,g,the,terminal_score,datetime.datetime.fromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S').split()[1])
				if terminal_score>2.23 and fool1==0:
					fool1=1
					ttx.append(i)
					tty.append(terminal_score)
			if ips=='172.16.99.204' and terminal_score>2.0 and fool1==0:
				print(i,ips,a,b,g,the,terminal_score,datetime.datetime.fromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S').split()[1])

				fool1=1
				ttx.append(i)
				tty.append(terminal_score)

			if fool1==0:				
				ttx.append(i)
				tty.append(terminal_score)

		
		#print(ttx,tty)
		tplot[minx]=np.mean(tty)
		minx=minx+tperiod


	# if ips=='172.16.99.204':
	# 	tplot,wflag=warning(tplot,wflag,"HIGH")
	# else:
	# 	tplot,wflag=warning(tplot,wflag,"LOW")
	
	#ax.plot(tplot.keys(),[tplot[i] for i in tplot],label=ips)
	
	
	if ips=='172.16.68.31':
		gap=1300
		plt.xticks(tplot.keys()[::gap],[datetime.datetime.fromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S').split()[1] for i in tplot.keys()][::gap],rotation=12)
	
	if ips=='172.16.68.31':
		for i in tplot:
			if i>1491670858:
				if fool==0:
					ax.scatter(i-2,tplot[i],color='k',s=10)
					fool=tplot[i]
				else:
					del tplot[i]

	# ax.plot(tplot.keys(),[tplot[i] if tplot[i]<0.25 else 0.25 for i in tplot],label=ips)
	ax.plot(tplot.keys(),[tplot[i] for i in tplot],label=ips)

for x,y,text in zip([1491656380,1491656583,1491669443,1491669643,1491670858,1491673592],[0.28,0.28,0.58,0.28,1.10,0.80],["A","B","C","D","E","F"]):   
	ax.annotate(text, (x+100,y+1.75),size=9)					
ax.legend(loc="upper right")

# ax.axhline(y=.1, linewidth=.5, color = 'r')
# ax.axhline(y=0, linewidth=.5, color = 'b')


# print(tplot.keys())
# plt.title("Realtime Aggregated Network Monitoring without Prevention or AAT(2) ")
plt.xlabel("Timestamp (in secs)")
plt.ylabel("Terminal Score")
plt.ylim(-0.1,4.5)
#plt.ylim(0,0.25)
plt.xlim(1491656200,None)
#plt.show()
plt.savefig("tscorep.png", bbox_inches='tight')

# print(ndata.keys())




