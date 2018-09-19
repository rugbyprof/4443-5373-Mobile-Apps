import { TestBed } from '@angular/core/testing';

import { VideoDataService } from './video-data.service';

describe('VideoDataService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: VideoDataService = TestBed.get(VideoDataService);
    expect(service).toBeTruthy();
  });
});
