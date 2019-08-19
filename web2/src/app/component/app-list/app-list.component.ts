import { LinuxApp } from '../../data/dto/linux-app';
import { Component, Input } from '@angular/core';
import { faChevronLeft } from '@fortawesome/free-solid-svg-icons';
import { faChevronRight } from '@fortawesome/free-solid-svg-icons';

const CAPACITY = 25;

@Component({
  selector: 'app-app-list',
  templateUrl: './app-list.component.html',
  styleUrls: ['./app-list.component.css']
})
export class AppListComponent {

  @Input() title: string;

  private appList: LinuxApp[];

  @Input()
  set apps(apps: LinuxApp[]) {
    const len = apps.length;
    this.list = apps.slice(0, len < CAPACITY ? len : CAPACITY);
    this.appList = apps;
  }

  list: LinuxApp[] = [];

  readonly faChevronLeft = faChevronLeft;
  readonly faChevronRight = faChevronRight;

  position = 0;

  onPrevious() {
    if (this.position - 1 < 0) {
      this.position = 0;
    } else {
      this.position--;
    }
  }

  onNext() {
    if ((this.position + 1) > CAPACITY) {
      this.position = CAPACITY;
    } else {
      this.position++;
    }
  }

}
