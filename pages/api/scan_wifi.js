import * as iw from 'wireless-tools/iw';

export default async (req, res) => {
	iw.scan('wlan0' ,function (error, networks) {
		if (error) {
			console.log(error);
			res.status(500).json({ error: 'Internal Server Error' });
		}

		else {
			console.log(networks);

			const ssid_list = networks.map(({ ssid }) => { return { name: ssid } });
			res.status(200).json({ ssid_list });
		}
	})
}