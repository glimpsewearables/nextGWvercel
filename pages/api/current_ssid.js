<<<<<<< HEAD
import * as iwconfig from 'wireless-tools/iwconfig';

export default async (req, res) => {
	iwconfig.status('wlan0' ,function (error, status) {
		if (error) {
			console.log(error);
			res.status(500).json({ error: 'Internal Server Error' });
		}   

		else {
		

			//const ssid_list = status.map(({ ssid }) => { return { name: ssid } });
			res.status(200).json(status.ssid);
		}
	})
}

 

=======
import * as iwconfig from 'wireless-tools/iwconfig';

export default async (req, res) => {
	iwconfig.status('wlan0' ,function (error, status) {
		if (error) {
			console.log(error);
			res.status(500).json({ error: 'Internal Server Error' });
		}

		else {
			console.log(status);

			const ssid_list = status.map(({ ssid }) => { return { name: ssid } });
			res.status(200).json({ ssid_list });
		}
	})
}

 

>>>>>>> 2f6d3cf0a88741e94528ff45d7141f5939f1aacf
