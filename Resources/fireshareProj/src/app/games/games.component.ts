import { Component, OnInit } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection, AngularFirestoreDocument } from 'angularfire2/firestore';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

interface Game {
  id:string,
  publisher:string,
  genres:string,
  coop:string,
  name:string,
  timestamp:string,
  system:string,
  releaseDate:string,
  players:string,
  reviewRating:string,
  esrbRating:string,
  developer:string
}

@Component({
  selector: 'app-games',
  templateUrl: './games.component.html',
  styleUrls: ['./games.component.css']
})

export class GamesComponent implements OnInit {

  gamesCol: AngularFirestoreCollection<Game>;
  games: Observable<Game[]>;

  constructor(private afs: AngularFirestore) {

  }

  ngOnInit() {
    this.gamesCol = this.afs.collection('games');
    this.games = this.gamesCol.valueChanges();
  }

}
