import { LinuxAppService } from './service/linux-app.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import {MatButtonModule} from '@angular/material/button';
import { HomeComponent } from './component/home.component';
import { HttpClientModule } from '@angular/common/http';
import { AppListComponent } from './component/app-list/app-list.component';
import {MatCardModule} from '@angular/material/card';
import { LinuxAppComponent } from './component/linux-app/linux-app.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { TitlePipe } from './pipe/title.pipe';
import { SearchPipe } from './pipe/search.pipe';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    AppListComponent,
    LinuxAppComponent,
    TitlePipe,
    SearchPipe
  ],
  imports: [
    MatButtonModule,
    MatListModule,
    MatIconModule,
    MatSidenavModule,
    MatToolbarModule,
    BrowserAnimationsModule,
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    MatCardModule,
    FontAwesomeModule
  ],
  providers: [
    LinuxAppService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
