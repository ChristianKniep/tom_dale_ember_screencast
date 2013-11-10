App = Ember.Application.create({});



App.Store = DS.Store.extend({
	revision: 12,
	//adapter: 'DS.FixtureAdapter',
  	adapter: DS.RESTAdapter.extend({
    	url: 'http://localhost:8082'
  })
});

App.Router.map(function() {
  this.resource('pins', function() {
  	this.resource('pin', { path: ':pin_id' })
  });
  this.resource('about');
});


App.PinsRoute = Ember.Route.extend({
	model: function() {
		return App.Pin.find();
	}
});

App.PinController = Ember.ObjectController.extend({
  isEditing: false,
  startEditing: function() {
    this.set('isEditing', true);
  },
  doneEditing: function (){
    this.set('isEditing', false);
  }
});


App.Pin = DS.Model.extend({
	pinnr: DS.attr('string'),
	status: DS.attr('string'),
	name: DS.attr('string'),
	changedAt: DS.attr('date'),
});

App.Pin.FIXTURES =[{
	id: 1,
	pinnr: "1",
    name: "TestPin1", 
    status: "0", 
    changedAt: new Date("2013-11-10")
}, {
	id: 2,
	pinnr: "2",
    name: "TestPin2", 
    status: "0", 
    changedAt: new Date("2013-11-09")
}];

Ember.Handlebars.registerBoundHelper('date', function(date) {
  return moment(date).fromNow();
});
