### Requirements

- Simulate a plate transport system and implement a corresponding data structure.
- In this simulation, plates with same width and height but different thicknesses are carried from one point to another.
- Plates have integer thicknesses between 1 and 9.
- Crates have an integer capacity between 9 and 99, in terms of total thicknesses of contained plates. For example, a crate with capacity 20 can carry plates with thicknesses [9,9,2], [8] or [7,8,4], but cannot carry [9,9,3] where the total thickness exceeds the capacity.
- There are two points, source and destination, that plates are transported.
- There are two conveyor rollers (belts) that carry crates. One conveyor is used to carry empty crates, other to carry the crates containing plates. Conveyors can carry any number of crates, there is no upper limit for it.
- At the source point, a robot arm places plates to the available crate one by one (if exists) and feeds the crate to the conveyor roller heading from source to destination called source-to- dest conveyor. Here is the complete algorithm:
  * When a plate is to be added, robot first checks whether there is an existing crate at the source point.
  * If there is an existing crate at the source point, it first checks its remaining capacity. If there is no suﬃcient capacity in the existing crate, it feeds the crate to the       source-to-dest conveyor.
  * If there is no crate at the source point, it tries to get one crate from dest-to-source conveyor (which carries empty crates).
  * If it can successfully place the plate and crate is full, it immediately feeds the crate to the source-to-dest conveyor.
  * When no plate could be placed to any crate, unsuccessful attempt should be indicated (i.e. corresponding method returns False, see design requirements).
- At the destination point, another robot arm removes plates from the incoming crates one by one and when a crate is empty, it feeds it to another conveyor roller heading from destination to source called dest-to-source conveyor. Here is the complete algorithm:
  * When a plate is to be removed, robot first checks whether there is an existing crate at the destination point.
  * If there is no crate at the destination point, it should try to to get one crate from source-to-dest conveyor.
  * If a plate is removed, the thickness of the plate should be indicated (returned). 
  * If no plate is removed, zero should be returned.
  * When a crate is empty (after the removal), it immediately feeds the empty crate to the dest-to-source conveyor.
- During the filling operation at the source point, maximum number of plates possible is tried to be sent. For example, if the crate capacity is 20, crate with plates [9,9,2] will immediately be fed to the conveyor, however if the contained plates is [9,9,1], robot waits for the next plate to be send. If the next plate has a tickness of 1, it will also be placed to the crate (because capacity is enough) and sends the crate to the conveyor. On the other hand, if the next plate has a thickness of 5, the robot first sends the existing crate to the conveyor and fetches another empty conveyor from the dest-to-source conveyor.
- Source-to-dest conveyor carries non-empty crates only. 
- Dest-to-source conveyors carries empty crates only.
