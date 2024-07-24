# ARF
ARF is a simple python based rendering farm manager for blender

# TODO

## For MVP
- [ ] cli interface
- [x] slave connect to master
- [ ] rendering command
  - [x] send blend
  - [ ] calculate task distribution
    - [ ] stills
    - [ ] animations
  - [ ] start render job
  - [ ] send result to master
  - [ ] master composit
- [ ] config file for
  - [ ] blender installation location
  - [ ] blendfile path (master and slave)
  - [ ] networking stuff
  - [ ] render output (master and slave)

# For v0.2
- [ ] gui interface
- [ ] rendering command
  - [ ] validate blend
  - [ ] error handling
  - [ ] distribute tasks reletive to mesured speed of machine
  - [ ] configurable batch size of frames 
- [ ] config file for
  - [ ] render speed estemate config and override
- [ ] slave status reports
- [ ] remote control of slaves
      
