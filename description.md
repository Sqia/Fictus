## Inspiration
Usually my or my family whatsapps group shared news. Sometimes the news is fake and sometimes is valid, from that story i got an idea. To make check validity of the news practical and fast. That when i thought about fictus, to check news validity via whatsapps bot. Fictus is the latin word of fake
## What it does
It reads your message/news that you want to check, and gives a response depending on the message/news
## How we built it
I built it using machine learning, using the python library scikit-learn. I first gather the data, i get the data from the Mafindo api https://mafindodocs.netlify.app/ and Mendeley https://data.mendeley.com/datasets/p3hfgr5j3m/1 these data provider really helped me and provide thousand of news to train my machine learning models. After we train the models we save it, then create a server that will handle twilio api for whatsapps and running the model. Then we deploy it to a public url server so twilio whatsapps api can listen and interact with our server. So twilio will receive the message from whatsapps then forward it to our server, after that our server will run the model and predict the news validity. Then the prediction will be send to the user via the twilio api.
## Challenges we ran into
- Data scramble, the data encoding, unicode, structure is messy (i need to clean and format the data first before training the data this was painful and time consuming)
- Unreliable deployment (server/hardware issue, lack of computing power)
- To much to do (i am doing this solo with no team, i have a limited stamina)
## Accomplishments that we're proud of
- Be able to predict the validity of the news
- Know what type of fake news that we predict
- Being scalable as long as the hardware/server components is good
- Run on a production server
- Able to interact with the twilio whatsapps api
- Accessible to a lot of people as long as we have the infrastructure
## What we learned
- At first i thought training machine learning model will take hours, but no it actually takes seconds out
- Learning about scikit learn and the available training method
- Deploy a public and production server using flask and gunicorn
- How easy it is to create a model
- Data analyzing and format/cleaning data (because the data was messy)
- Being able to manage time
- Understanding the twilio api and webhook
- Seiing machine interpretation of news
- Knowing file format like json, csv and how they works
## What's next for fictus
- More accurate news predictions (The accuracy is 81% currently)
- Get scaleable (Get better hardware and server component)
- Make it more accessible to a lot more people
- Improve the machine learning training methods
- Make the code cleaner and readable
