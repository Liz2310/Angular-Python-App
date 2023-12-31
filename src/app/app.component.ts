import { Component, OnInit } from '@angular/core';
import { RestService } from './rest.service';
import { Weather } from './Weather';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'TEST_2';

  constructor(private rs : RestService){}

  headers = ["day","temperature", "windspeed",  "event"]

  weather : Weather[] = [];

  ngOnInit()
  {
        this.rs.readWeather()
        .subscribe
          (
            (response) => 
            {
              this.weather = response[0]["data"];
            },
            (error) =>
            {
              console.log("No Data Found" + error);
            }

          )
  }
}
