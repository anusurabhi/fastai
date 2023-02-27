import gradio as gr

def greet(name):
    return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
#/export
from fastai.vision.all import *
import gradio as gr

learn = load_learner('flag_model.pkl')
categories = ('Afghanistan',	'Albania',	'Algeria',	'Andorra',	'Angola',	'Antigua and Barbuda',	'Argentina',	'Armenia',	'Australia',	'Austria',	'Azerbaijan',	'Bahamas',	'Bahrain',	'Bangladesh',	'Barbados',	'Belarus',	'Belgium',	'Belize',	'Benin',	'Bhutan',	'Bolivia',	'Bosnia and Herzegovina',	'Botswana',	'Brazil',	'Brunei',	'Bulgaria',	'Burkina Faso',	'Burundi',	'Côte d Ivoire',	'Cabo Verde',	'Cambodia',	'Cameroon',	'Canada',	'Central African Republic',	'Chad',	'Chile',	'China',	'Colombia',	'Comoros',	'Congo (Congo-Brazzaville)',	'Costa Rica',	'Croatia',	'Cuba',	'Cyprus',	'Czechia (Czech Republic)',	'Democratic Republic of the Congo',	'Denmark',	'Djibouti',	'Dominica',	'Dominican Republic',	'Ecuador',	'Egypt',	'El Salvador',	'Equatorial Guinea',	'Eritrea',	'Estonia',	'Eswatini',	'Ethiopia',	'Fiji',	'Finland',	'France',	'Gabon',	'Gambia',	'Georgia',	'Germany',	'Ghana',	'Greece',	'Grenada',	'Guatemala',	'Guinea',	'Guinea-Bissau',	'Guyana',	'Haiti',	'Holy See',	'Honduras',	'Hungary',	'Iceland',	'India',	'Indonesia',	'Iran',	'Iraq',	'Ireland',	'Israel',	'Italy',	'Jamaica',	'Japan',	'Jordan',	'Kazakhstan',	'Kenya',	'Kiribati',	'Kuwait',	'Kyrgyzstan',	'Laos',	'Latvia',	'Lebanon',	'Lesotho',	'Liberia',	'Libya',	'Liechtenstein',	'Lithuania',	'Luxembourg',	'Madagascar',	'Malawi',	'Malaysia',	'Maldives',	'Mali',	'Malta',	'Marshall Islands',	'Mauritania',	'Mauritius',	'Mexico',	'Micronesia',	'Moldova',	'Monaco',	'Mongolia',	'Montenegro',	'Morocco',	'Mozambique',	'Myanmar',	'Namibia',	'Nauru',	'Nepal',	'Netherlands',	'New Zealand',	'Nicaragua',	'Niger',	'Nigeria',	'North Korea',	'North Macedonia',	'Norway',	'Oman',	'Pakistan',	'Palau',	'Palestine State',	'Panama',	'Papua New Guinea',	'Paraguay',	'Peru',	'Philippines',	'Poland',	'Portugal',	'Qatar',	'Romania',	'Russia',	'Rwanda',	'Saint Kitts & Nevis',	'Saint Lucia',	'Saint Vincent & the Grenadines',	'Samoa',	'San Marino',	'Sao Tome & Principe',	'Saudi Arabia',	'Senegal',	'Serbia',	'Seychelles',	'Sierra Leone',	'Singapore',	'Slovakia',	'Slovenia',	'Solomon Islands',	'Somalia',	'South Africa',	'South Korea',	'South Sudan',	'Spain',	'Sri Lanka',	'Sudan',	'Suriname',	'Sweden',	'Switzerland',	'Syria',	'Tajikistan',	'Tanzania',	'Thailand',	'Timor-Leste',	'Togo',	'Tonga',	'Trinidad & Tobago',	'Tunisia',	'Turkey',	'Turkmenistan',	'Tuvalu',	'Uganda',	'Ukraine',	'United Arab Emirates',	'United Kingdom',	'United States of America',	'Uruguay',	'Uzbekistan',	'Vanuatu',	'Venezuela',	'Vietnam', 'Yemen',	'Zambia')
def classify_image(img):
  pred, idx, probs = learn.predict(img)
  return dict(zip(categories, map(float,probs)))

image = gr.inputs.Image(shape=(192, 192))
label = gr.outputs.Label()
intf = gr.Interface(fn=classify_image, inputs=image, outputs=label)
intf.launch(inline=False)
