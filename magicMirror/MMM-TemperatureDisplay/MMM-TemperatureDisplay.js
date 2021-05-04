Module.register("MMM-TemperatureDisplay", {
  defaults: {},

  start: function (){
    Log.log("Starting module: " + this.name);

    this.updateTimer = null;
    this.temperature = 0;

    const url = "http://" + this.config.bridgeIp + "/api/" + this.config.user + "/sensors/8/";
    this.req = new Request(url, {method: "GET"});

    this.scheduleUpdate(1 * 1000) // schedule initial update in 1s
  },

  scheduleUpdate: function (delay) {
		clearTimeout(this.updateTimer);

    var self = this;
		this.updateTimer = setTimeout(function () {
			self.updateTemperature();
		}, delay);
	},

  updateTemperature: function () {
    fetch(this.req)
      .then( response => response.json())
      .then( data => {
        this.temperature = data.state.temperature / 100; // sensor in centi-Celsius
        this.scheduleUpdate(5*1000) // schedule next update in 10 minutes
      });

      this.sendNotification("INDOOR_TEMPERATURE", this.temperature);
  },


})

