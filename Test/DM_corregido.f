 ! Se corrigieron las subrutinas fcc, pbc. Valores 105 --> 200
 ! P10: MD for Lennard-Jones particles
 !
       program DM
       implicit real*8(a-h,o-z)

       parameter (n=1372, ngrx=1000)
       dimension x(n),y(n),z(n)
       dimension vx(n),vy(n),vz(n)
       dimension fx(n),fy(n),fz(n)
       dimension ig(1000)

        real*4 r
        common gr(ngrx)
        
        open (1, file = 'gr.dat')
        open (2,file='conf.dat',status='unknown')

        rho = 1.0
        T=1.12
        npasos=10000

        dum = 17367d0
        pi = 4d0 * datan(1d0)

         call fcc(n, rho, x, y, z, aL, aL, aL)

         do i=1,n
          vr = dsqrt(3*T)
          call ggub(dum,r)
          cost = 2*r-1
          sint = dsqrt(1-cost**2)
         call ggub(dum,r)
          fi = r*2*pi
          vx(i) = vr*sint*dcos(fi)
          vy(i) = vr*sint*dsin(fi)
          vz(i) = vr*cost
         end do

        aL2 = aL/2d0
        cut2 = (2.5d0)**2
        cutr2 = (aL/2)**2
        ngr = 200d0
        hgr = aL2/ngr
        dt = 0.01d0
        
        print*,n/aL**3,aL2,hgr
        !pause

        ec = 0
        u = 0
        ap = 0

        do i = 1,1000
         ig(i) = 0
         gr(i) = 0
        end do

       do k = 1,npasos
       
       !print*,k
       !pause
       
       
        do i = 1, n
         call pbc(x(i),y(i),z(i),aL,aL,aL)
        end do

        do i = 1, n
          fx(i) = 0
          fy(i) = 0
          fz(i) = 0
        end do

        epot=0

       do i = 1, n-1
         xi = x(i)
         yi = y(i)
         zi = z(i)
        do j = i+1, n
          xx = xi-x(j)
          yy = yi-y(j)
          zz = zi-z(j)
         call mic (xx,yy,zz,aL,aL,aL)
           r2 = xx**2+yy**2+zz**2
          if (r2 .lt. cut2) then
           r1 = 1/r2
           r6 = r1**3
           pot=4*r6*(r6-1)
            u = u+pot
            epot=epot+pot
              rr = 48*r6*r1*(r6-0.5d0)
            fxx = rr*xx
            fyy = rr*yy
            fzz = rr*zz
            ap = ap+rr*r2

            fx(i) = fx(i)+fxx
            fy(i) = fy(i)+fyy
            fz(i) = fz(i)+fzz
             fx(j) = fx(j)-fxx
             fy(j) = fy(j)-fyy
             fz(j) = fz(j)-fzz
           end if
        end do
       end do

	ekin=0
       do i=1,n
         vxi = vx(i)+dt*fx(i)
         vyi = vy(i)+dt*fy(i)
        vzi = vz(i)+dt*fz(i)
        vxx = 0.5d0*(vxi+vx(i))
        vyy = 0.5d0*(vyi+vy(i))
        vzz = 0.5d0*(vzi+vz(i))
         en = vxx**2+vyy**2+vzz**2

        ekin = ekin+en
        ec = ec+en
        vx(i) = vxi
        vy(i) = vyi
        vz(i) = vzi
         x(i) = x(i)+dt*vx(i)
         y(i) = y(i)+dt*vy(i)
         z(i) = z(i)+dt*vz(i)
       end do

           write(2,*) x(5),y(5),z(5)
           
	  call Mgdr(n,x,y,z,aL,aL,aL)

      end do

        temp =ec/(3*n*npasos)
        u = u/(n*npasos)
        ap = rho*temp+ap/(3*aL**3*npasos)

         write(*,*) 'temperature=',temp
         write(*,*) 'energy=',u
         write(*,*) 'pressure=',ap

        do k=1,ngr
         r=(k-1)*hgr+hgr/2.d0
         vol=4*pi/3*((r+hgr/2d0)**3-(r-hgr/2d0)**3)
         gdr=gr(k)/(n*((n-1)/aL**3)*npasos*vol)
!        gdr=gr(k)/(n*(n-1)/1.d0**3*npasos*vol)  ! quitando aL -> gr menor que uno
        write(1,*) r,gdr
        end do
        

        Close(1)
        Close(2)

      end program DM

!*************************************************************************************
   !
   ! Generation of fcc lattice
   !
      subroutine fcc(lmn, dens, r1x, r1y, r1z, xlx, yly, zlz)

      implicit real*8 (a-h, o-z)
      parameter (num = 1372)

       dimension r1x(num), r1y(num), r1z(num)
       dimension sx(4), sy(4), sz(4)

        data sx /0d0, 0.5d0, 0.5d0, 0d0/
        data sy /0d0, 0.5d0, 0d0, 0.5d0/
        data sz /0d0, 0d0, 0.5d0, 0.5d0/

        data sh /0.01d0/

       a = (4d0/dens)**(1d0/3d0)
       n = (lmn/4)**(1d0/3d0) + 0.001

       xlx = n*a
       yly = n*a
       zlz = n*a

       m = 1
         do i = 1, n
         do j = 1, n
         do k = 1, n
         do l = 1, 4
            r1x(m) = (i - 1 + sx(l) + sh) * a - xlx/2
            r1y(m) = (j - 1 + sy(l) + sh) * a - yly/2
            r1z(m) = (k - 1 + sz(l) + sh) * a - zlz/2
         m=m+1
        end do
        end do
        end do
        end do

      end subroutine
      
      
 !
 !    Periodic boundary conditions
 !
      subroutine pbc(r1x,r1y,r1z,xlx,yly,zlz)

      implicit real*8 (a-h,o-z)

      r1x=r1x-xlx*dnint(r1x/xlx)
      r1y=r1y-yly*dnint(r1y/yly)
      r1z=r1z-zlz*dnint(r1z/zlz)

      end subroutine



 !
 !    Minimum image convention
 !
      subroutine mic(xx,yy,zz,xlx,yly,zlz)

      implicit real*8(a-h,o-z)

      xx=xx-xlx*dnint(xx/xlx)
      yy=yy-yly*dnint(yy/yly)
      zz=zz-zlz*dnint(zz/zlz)
      end subroutine



 !
 !    P1: Random number generator
 !
      subroutine ggub(dseed,r)

      real*8 z,d2p31m,d2pn31,dseed
      data d2p31m/2147483647./,d2pn31/2147483648./

      z = dseed
      z = dmod(16807.*z,d2p31m)
      r = z / d2pn31
      dseed = z
      end subroutine
      
      
      
      
      subroutine Mgdr(lmn,r1x,r1y,r1z,xlx,yly,zlz)

      implicit real*8(A-H,O-Z)
      parameter (num=256, ngrx=1000)

      dimension r1x(num), r1y(num), r1z(num)
      
      common gr(ngrx)
      !data hr /0.033d0/

      aL2 = xlx/2.0d0
      hr = aL2/200d0

      do i = 1, lmn-1
      do j = i + 1,lmn
         xx = r1x(i) - r1x(j)
         yy = r1y(i) - r1y(j)
         zz = r1z(i) - r1z(j)
       call mic (xx,yy,zz,xlx,yly,zlz)
         r = xx*xx + yy*yy + zz*zz
         rr = dsqrt(r)
       if (rr .lt. xlx/2) then
         k = rr/hr + 1
         gr(k) = gr(k) + 2
         !print*,k,gr(k)
       end if
      end do
      end do

      end subroutine
