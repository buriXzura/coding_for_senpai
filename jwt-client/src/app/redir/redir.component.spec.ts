import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RedirComponent } from './redir.component';

describe('RedirComponent', () => {
  let component: RedirComponent;
  let fixture: ComponentFixture<RedirComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RedirComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RedirComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
