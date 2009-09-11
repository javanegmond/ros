class update_test_rosbagmigration_MigratedMixed_5568494133a082ad58ef1aa391f47e2b(MessageUpdateRule):
	old_type = "test_rosbagmigration/MigratedMixed"
	old_full_text = """
Header             header
MigratedImplicit   field1 #(34, 16.32, "kjljene", (17, 58.2, "aldfkja", 82))


================================================================================
MSG: roslib/Header
#Standard metadata for higher-level flow data types
#sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: test_rosbagmigration/MigratedImplicit
Header  header
int32   field1 #34
float32 field2 #16.32
string  field3 #"kljene"
MigratedExplicit field4 #(17, 58.2 "aldfkja", 82)

================================================================================
MSG: test_rosbagmigration/MigratedExplicit
Header  header
int32   field1 #17
float32 field2 #58.2
string  field3 #"aldfkja"
int32   field4 #82
"""

	new_type = "test_rosbagmigration/MigratedMixed"
	new_full_text = """
Header             header
MigratedImplicit   field1 #((17, 58.2, "aldfkja", 82), "kjljene", 16.32, 34)
int32              field2 #59

================================================================================
MSG: roslib/Header
#Standard metadata for higher-level flow data types
#sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: test_rosbagmigration/MigratedImplicit
Header  header
MigratedExplicit field4 #(17, 58.2 "aldfkja", 82)
string  field3 #"kljene"
float32 field2 #16.32
int32   field1 #34



================================================================================
MSG: test_rosbagmigration/MigratedExplicit
Header  header
int32   afield1 #17
float32 afield2 #58.2
string  afield3 #"aldfkja"
int32   afield4 #82
"""

	order = 0
	migrated_types = [
		("Header","Header"),
		("MigratedImplicit","MigratedImplicit"),

	]

	valid = True

	def update(self, old_msg, new_msg):
		self.migrate(old_msg.header, new_msg.header)
		self.migrate(old_msg.field1, new_msg.field1)
		new_msg.field2 = 59

