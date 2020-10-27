import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChngpswdComponent } from './chngpswd.component';

describe('ChngpswdComponent', () => {
  let component: ChngpswdComponent;
  let fixture: ComponentFixture<ChngpswdComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ChngpswdComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ChngpswdComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
