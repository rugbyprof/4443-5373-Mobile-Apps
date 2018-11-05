import { Pipe, PipeTransform } from '@angular/core';
import { FirebaseProvider } from '../../providers/firebase/firebase';
import { Observable, from } from 'rxjs';

@Pipe({
  name: 'doc'
})
export class DocPipe implements PipeTransform {

  constructor(private db: FirebaseProvider) {}

  transform(value: any): Observable<any> {
    return this.db.doc$(value.path)
  }

}


/**
 * Usage:
 * 
 * <div *ngIf="noteDoc | async as note">
 * {{ (note.user | doc | async)?.name }}
 * </div>
 */