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
  selector: 'games-list',
  templateUrl: 'games-list.component.html',
  styles: []
})

// export class GamesListComponent implements OnInit {
  
//   gamesObservable: Observable<any[]>;
//   constructor(private db: AngularFireDatabase) { }
//   ngOnInit() {
//     this.gamesObservable = this.getGames('/games');
//   }
//   getGames(listPath): Observable<any[]> {
//     return this.db.list(listPath).valueChanges();
//   }
// }

export class GamesListComponent {
  

  gamesCol: AngularFirestoreCollection<Game>;
  games: Observable<Game[]>;

  constructor(private afs: AngularFirestore) {

  }

  ngOnInit() {
    this.gamesCol = this.afs.collection('games');
    this.games = this.gamesCol.valueChanges();
  }

}