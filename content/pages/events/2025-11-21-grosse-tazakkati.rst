:title: Double seminar: Bastien Grosse and Zoubaïr Tazakkati
:category: event
:date: 2025-11-21 14:00
:place: Salle de conférence CMAP (aile5, 2e étage)
:speaker: Bastien Grosse (LMJL - Nantes Université) et Zoubaïr Tazakkati (CMAP)
:shortdescription: Exposé dans le cadre du séminaire HPC@Maths.


.. rubric:: *Par Bastien Grosse*

*Well-posedness of the Vlasov-Poisson system with floating potential at a
wall.*

We are interested in a bi-species, uni-dimensional plasma occupying the
domain [0,1]. Particles are injected at x=0 and at x=1 there is a fully
absorbing wall.  If we want to model the problem by the Vlasov-Poisson
system, then we have to choose a boundary condition for the potential.
The system is compatible with  the Maxwell-Ampère equation only for a
nonlinear Dirichlet boundary condition at the wall, which depends on
currents.  This expression for the floating potential is naturally
associated with finite energy solutions. We will study well-posedness of
the system in the space BV.
Then, we will show simulations.
If the time permits, we will finish by discussing steady-states.



.. rubric:: *Par Zoubaïr Tazakkati*

*Electron-Ion Plasmas in Strong Electromagnetic Fields: A Gyrokinetic/Gyromoment Approach*


We study a coupled electron-ion plasma governed by the Boltzmann-Poisson equations in a regime where intense electric and magnetic fields dominate. Although the configuration under study remains generic, it is strongly inspired by the physical conditions encountered in Hall effect thrusters. A scaling analysis reveals that electrons undergo complex dynamics: they combine an ExB drift with a rapid cyclotron gyration around the magnetic field lines, which leads to their trapping along these lines. In contrast, the ions remain weakly magnetized but are strongly accelerated by the electric field. This multiscale behavior introduces significant numerical stiffness in the governing partial differential equations, mainly (though not exclusively) due to the very fast electron gyromotion.


To describe these dynamics, we propose a global and innovative strategy for the electrons. At the kinetic level, we perform a Hilbert expansion of the electron distribution function. This analysis naturally separates the distribution into a leading-order component corresponding to the gyroaveraged equilibrium (i.e., the averaged dynamics of the trajectories once the fast cyclotron oscillations have been filtered out) and higher-order oscillatory perturbations that carry the information of the fast cyclotron motion. Building on this decomposition, we introduce a moment-based fluid reduction. The underlying polynomial basis is carefully designed to reflect the structure of the kinetic distribution, distinguishing the gyroaveraged contribution from its oscillatory corrections. The resulting “gyromoment” model thus preserves the essential anisotropies of the strongly magnetized regime. The ions are also described using a fluid model, leading to a fully fluid electron-ion description. In contrast to the electrons, the ion fluid model follows the standard Euler-like formulation, as their weak magnetization does not require gyro-reduction.


Finally, we provide numerical test cases to highlight the key dynamics observed in the system.