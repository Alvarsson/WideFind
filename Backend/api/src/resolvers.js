import axios from 'axios';

export const resolvers = {
    Event: {
        content(object, params, context, resolveInfo) {
            const url = `${process.env.OBSERVER_IP}/`;
            console.log({url});
            axios.post(url, {
                event: object.content
              })
              .then(response => {
                console.log({response});
              })
              .catch(error => {
                console.log({error});
              });
            return object.content;
        }
    }
};