/* Magic Mirror Config Sample
 *
 * By Michael Teeuw https://michaelteeuw.nl
 * MIT Licensed.
 *
 * For more information on how you can configure this file
 * See https://github.com/MichMich/MagicMirror#configuration
 *
 */

var config = {
	address: "localhost", 	// Address to listen on, can be:
							// - "localhost", "127.0.0.1", "::1" to listen on loopback interface
							// - another specific IPv4/6 to listen on a specific interface
							// - "0.0.0.0", "::" to listen on any interface
							// Default, when address config is left out or empty, is "localhost"
	port: 8080,
	basePath: "/", 	// The URL path where MagicMirror is hosted. If you are using a Reverse proxy
					// you must set the sub path here. basePath must end with a /
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"], 	// Set [] to allow all IP addresses
															// or add a specific IPv4 of 192.168.1.5 :
															// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
															// or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
															// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	useHttps: false, 		// Support HTTPS or not, default "false" will use HTTP
	httpsPrivateKey: "", 	// HTTPS private key path, only require when useHttps is true
	httpsCertificate: "", 	// HTTPS Certificate path, only require when useHttps is true

	language: "en",
	logLevel: ["INFO", "LOG", "WARN", "ERROR"], // Add "DEBUG" for even more logging
	timeFormat: 24,
	units: "metric",
	// serverOnly:  true/false/"local" ,
	// local for armv6l processors, default
	//   starts serveronly and then starts chrome browser
	// false, default for all NON-armv6l devices
	// true, force serveronly mode, because you want to.. no UI on this device

	modules: [
		{
			module: "alert",
		},
		{
			module: "updatenotification",
			position: "top_bar"
		},
		{
			module: "clock",
			position: "top_left"
		},
		{
			disabled: false,
			module: "calendar",
			header: "Kalender",
			position: "top_left",
			config: {
				calendars: [
					/*{
						symbol: "calendar-check",
						url: "webcal://www.calendarlabs.com/ical-calendar/ics/76/US_Holidays.ics"
					},*/
					{
						symbol: "calendar-check",
						url: "https://kalender.link/ical/best"
					}
				],
				//selfSignedCert: true
			}
		},
		{
			module: "MMM-Namnsdag",
			position: "top_left",
			header: "Namnsdag"
		},
		{
			module: "weather",
			position: "top_right",
			config: {
				type: "current",
				showIndoorTemperature: true,
				/* Open Weather Map */
				//weatherProvider: openweathermap,
				location: "Göteborg",
				locationID: "",
				apiKey: "9cab403720f3d1dfd158dcbfc27c194b"
			}
		},
		{
			//disabled: true,
			module: 'mmm-weatherchart',
			position: 'top_right', // this can be any of the regions
			config: {
				country: 'Sweden', // as determined above
				area: 'Västra%20Götaland', // as determined above
				city: 'Gothenburg', // as determined above
				updateInterval: 60 * 60 * 1000, // update every hour
				hideBorder: true, // whether or not a border with city name should be shown
				negativeImage: true, // whether or not the default white image should be inverted
				hoursToShow: 24, // Cut the image down to show less than the full 48 hour forecast. -1 to show everything.
				//mmDirectory: "/home/pi/MagicMirror/" // required for caching; adjust if it differs
			}
		},
		{
			module: "MMM-TemperatureDisplay",
			config: {
				bridgeIp: "192.168.88.254",
				user: "nUcg5selpK4M3EjTxkvAneq1G6hddvShFULC0eUO"
			}
		},
		{
			disabled: true,
			module: "compliments",
			position: "lower_third"
		},
		{
			module: "newsfeed",
			position: "lower_third",
			config: {
				feeds: [
					{
						title: "Svenska Dagbladet",
						url: "http://www.svd.se/?service=rss&type=latest"
					},
					{
						title: "Dagens Nyheter",
						url: "https://www.dn.se/rss/"
					}
				],
				showSourceTitle: true,
				showPublishDate: true,
				broadcastNewsFeeds: false,
				broadcastNewsUpdates: false,
				showDescription: true,
				wrapDescription: true
			}
		},
		{
			//disabled: true,
			module: "MMM-Vasttrafik-PublicTransport",
			position: "bottom_left",
			header: "Västtrafik",
			config:
			{
				myStops: // REQUIRED. An array of stop id's. Your are required to have at least one stop.
				[      // see 3. Get stops that you want to track.
					{
						id: "9021014007171000",
						filterAttr: "track", //Optional. Default is null, if set 'filterKey' also needs to be set. Allowed value: "track", "direction", "line" or "type"
						filterKey: "A"       //Optional. Default is null, if set 'filterAttr' also needs to be set. Filter key is any value of the filtered attribute, see filtered board.
					},
					{
						id: "9021014007172000",
						filterAttr: "track",
						filterKey: "B"
					},
				],
				appKey: "zELyDmhGqYlkX000OTR_SNTha7Ma",       // REQUIRED. see 1. Create application and obtain required client id and secret.
				appSecret: "Lrqpm0K1JbqRwNSOMFo1HDI3L8Ma", // REQUIRED. see 1. Create application and obtain required client id and secret.
				debug: false,                 // Optional. Enable some extra output when debugging.
				sortBy: "track",               // Optional. Sort your departure board by either "track", "direction", "line" or "type"
											// default is "track".
				refreshRate: "30000",          // Optional. Refresh rate int milliseconds, default is 60 seconds.
				trafficSituations: true,      // Optional. Default is false, you need a subscription to TrafficSituations v1 API please see Prerequisites 2.1
				board:
				{
					destination: { maxPxWidth: 150 },      // Optional. Force max width for destination names.
				},
				showTrackNumbers: false,     //Optional. Default is true, if set to false will hide the track column.
				//showStopHeader: false,       //Optional. Default is true, if set to false will hide the stop name header.
				showDestinationName: false,   //Optional. Default is true, if set to false will hide the direction/stop column.
				enableDepartureTimeColors: true, //Optional. Default is false, if set 'departureTimeColors' also needs to be set. See section "Departue time colors".
				departureTimeColors:
				[
					{
						max: 1,
						min: 0,
						color: "#660202"
					},
					{
						max: 4,
						min: 2,
						color: "#FF0000"
					},
					{
						max: 6,
						min: 4,
						color: "#FFF200"
					},
					{
						max: 15,
						min: 7,
						color: "#52FF33"
					}
				]
			}
		},
		{
			module: 'MMM-SystemStats',
			position: 'bottom_right', // This can be any of the regions.
			// classes: 'small dimmed', // Add your own styling. OPTIONAL.
			// header: 'System Stats', // Set the header text OPTIONAL
			config: {
				updateInterval: 10000, // every 10 seconds
				align: 'right', // align labels
				//header: 'System Stats', // This is optional
				units: 'metric', // default, metric, imperial
				view: 'textAndIcon',
			},
		},
	]
};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {module.exports = config;}
