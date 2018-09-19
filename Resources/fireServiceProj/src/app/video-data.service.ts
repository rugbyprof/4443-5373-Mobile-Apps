import { Injectable } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection, AngularFirestoreDocument } from 'angularfire2/firestore';
import { Observable } from 'rxjs';

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

@Injectable({
  providedIn: 'root'
})

export class VideoDataService {
  gamesCol: AngularFirestoreCollection<Game>;
  games: Observable<Game[]>;

  constructor(private afs: AngularFirestore) { }

  ngOnInit() {
    this.gamesCol = this.afs.collection('games');
    this.games = this.gamesCol.valueChanges();
    console.log(typeof(this.games));
  }

  getGames(){
    return this.games;
  }
}
