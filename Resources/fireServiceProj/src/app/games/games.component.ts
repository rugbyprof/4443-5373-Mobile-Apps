import { Component, OnInit } from '@angular/core';
import { VideoDataService } from '../video-data.service';


@Component({
  selector: 'app-games',
  templateUrl: './games.component.html',
  styleUrls: ['./games.component.css'],
  providers: [VideoDataService]
})

export class GamesComponent implements OnInit {

  games = [];

  constructor(private videoGameService: VideoDataService) {

  }

  ngOnInit() {
    this.games = this.videoGameService.games;
  }

}
