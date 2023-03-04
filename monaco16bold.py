width = const(11)
height = const(16)

data = [
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x00 (0)
	0x00,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x00,0x00,0x00,0x00,0x0c,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x01 (1)
	0x00,0x00,0x33,0x00,0x33,0x00,0x33,0x00,0x33,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x02 (2)
	0x00,0x00,0x19,0x80,0x19,0x80,0x19,0x80,0xff,0xc0,0x33,0x00,0x33,0x00,0x33,0x00,0x33,0x00,0xff,0xc0,0x66,0x00,0x66,0x00,0x66,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x03 (3)
	0x0c,0x00,0x3f,0x00,0x7c,0x00,0x6c,0x00,0x6c,0x00,0x3c,0x00,0x1c,0x00,0x0f,0x00,0x0f,0x80,0x0d,0x80,0x0d,0x80,0x6f,0x00,0x3e,0x00,0x0c,0x00,0x00,0x00,0x00,0x00, # Character 0x04 (4)
	0x00,0x00,0x78,0x60,0xcc,0xc0,0xcc,0xc0,0xcd,0x80,0xcf,0x00,0x7e,0x00,0x0f,0xc0,0x0e,0x60,0x1e,0x60,0x36,0x60,0x66,0x60,0xc3,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x05 (5)
	0x00,0x00,0x3c,0x00,0x66,0x00,0x66,0x00,0x6e,0x00,0x7c,0x00,0x38,0x00,0x79,0x80,0xcd,0x80,0xc7,0x80,0xc3,0x80,0xc7,0x80,0x7e,0xe0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x06 (6)
	0x00,0x00,0x0f,0x00,0x0f,0x00,0x0f,0x00,0x06,0x00,0x06,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x07 (7)
	0x03,0x80,0x0e,0x00,0x18,0x00,0x38,0x00,0x30,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x30,0x00,0x38,0x00,0x18,0x00,0x0e,0x00,0x03,0x80, # Character 0x08 (8)
	0x70,0x00,0x1c,0x00,0x06,0x00,0x07,0x00,0x03,0x00,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x03,0x00,0x07,0x00,0x06,0x00,0x1c,0x00,0x70,0x00, # Character 0x09 (9)
	0x0c,0x00,0x0c,0x00,0x7f,0x80,0x1e,0x00,0x1e,0x00,0x7f,0x80,0x0c,0x00,0x0c,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x0a (10)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x7f,0xe0,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x0b (11)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1c,0x00,0x1e,0x00,0x1e,0x00,0x06,0x00,0x0c,0x00,0x18,0x00, # Character 0x0c (12)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x7f,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x0d (13)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1e,0x00,0x1e,0x00,0x1e,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x0e (14)
	0x00,0xc0,0x00,0xc0,0x01,0x80,0x03,0x00,0x03,0x00,0x06,0x00,0x06,0x00,0x0c,0x00,0x18,0x00,0x18,0x00,0x30,0x00,0x60,0x00,0x60,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x0f (15)
	0x00,0x00,0x1e,0x00,0x33,0x80,0x61,0xc0,0x61,0xc0,0x63,0xc0,0x66,0xc0,0x6c,0xc0,0x6c,0xc0,0x78,0xc0,0x70,0xc0,0x31,0x80,0x1f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x10 (16)
	0x00,0x00,0x1c,0x00,0x3c,0x00,0x6c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x7f,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x11 (17)
	0x00,0x00,0x3f,0x80,0x60,0xc0,0x00,0xc0,0x00,0xc0,0x01,0x80,0x07,0x00,0x0e,0x00,0x18,0x00,0x30,0x00,0x70,0x00,0x60,0x00,0x7f,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x12 (18)
	0x00,0x00,0x3e,0x00,0x63,0x80,0x01,0x80,0x01,0x80,0x03,0x00,0x3f,0x00,0x01,0x80,0x00,0xc0,0x00,0xc0,0x00,0xc0,0x61,0x80,0x3f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x13 (19)
	0x00,0x00,0x03,0x00,0x07,0x00,0x0f,0x00,0x1b,0x00,0x1b,0x00,0x33,0x00,0x63,0x00,0xc3,0x00,0xff,0xe0,0x03,0x00,0x03,0x00,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x14 (20)
	0x00,0x00,0x7f,0x80,0x60,0x00,0x60,0x00,0x60,0x00,0x7e,0x00,0x03,0x80,0x00,0xc0,0x00,0xc0,0x00,0xc0,0x00,0xc0,0x61,0x80,0x3f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x15 (21)
	0x00,0x00,0x1f,0x80,0x30,0x00,0x60,0x00,0xe0,0x00,0xc0,0x00,0xdf,0x00,0xf1,0x80,0xe0,0xc0,0xe0,0xc0,0x60,0xc0,0x71,0x80,0x3f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x16 (22)
	0x00,0x00,0x7f,0xc0,0x00,0xc0,0x01,0x80,0x03,0x80,0x06,0x00,0x06,0x00,0x0c,0x00,0x0c,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x17 (23)
	0x00,0x00,0x1f,0x80,0x71,0xc0,0x60,0xc0,0x60,0xc0,0x31,0x80,0x1f,0x00,0x3b,0x80,0x71,0xc0,0x60,0xc0,0x60,0xc0,0x71,0xc0,0x1f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x18 (24)
	0x00,0x00,0x3f,0x00,0x63,0x80,0xc1,0x80,0xc1,0xc0,0xc1,0xc0,0x63,0xc0,0x3e,0xc0,0x00,0xc0,0x01,0xc0,0x01,0x80,0x03,0x00,0x7e,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x19 (25)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1e,0x00,0x1e,0x00,0x1e,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1e,0x00,0x1e,0x00,0x1e,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x1a (26)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1e,0x00,0x1e,0x00,0x1e,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1c,0x00,0x1e,0x00,0x1e,0x00,0x06,0x00,0x0c,0x00,0x18,0x00, # Character 0x1b (27)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x60,0x01,0xc0,0x07,0x00,0x1c,0x00,0x70,0x00,0x1c,0x00,0x07,0x00,0x01,0xc0,0x00,0x60,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x1c (28)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xff,0xc0,0x00,0x00,0x00,0x00,0xff,0xc0,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x1d (29)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x60,0x00,0x38,0x00,0x0e,0x00,0x03,0x80,0x00,0xe0,0x03,0x80,0x0e,0x00,0x38,0x00,0x60,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x1e (30)
	0x00,0x00,0x3f,0x80,0x00,0xc0,0x00,0xc0,0x01,0xc0,0x03,0x80,0x06,0x00,0x0c,0x00,0x18,0x00,0x18,0x00,0x00,0x00,0x00,0x00,0x18,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x1f (31)
	0x1f,0x00,0x31,0x80,0x60,0xc0,0xce,0x60,0xdb,0x60,0xd1,0x60,0xd1,0xe0,0xd9,0xe0,0xcf,0x40,0xc0,0x00,0x60,0x00,0x33,0x00,0x1f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x20 (32)
	0x00,0x00,0x0c,0x00,0x1e,0x00,0x1e,0x00,0x1e,0x00,0x3b,0x00,0x33,0x00,0x33,0x00,0x71,0x80,0x7f,0x80,0x61,0x80,0xe1,0xc0,0xc0,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x21 (33)
	0x00,0x00,0x7f,0x80,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x7f,0x80,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x7f,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x22 (34)
	0x00,0x00,0x1f,0x80,0x30,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x30,0x00,0x1f,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x23 (35)
	0x00,0x00,0x7f,0x00,0x61,0x80,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x61,0x80,0x7f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x24 (36)
	0x00,0x00,0x3f,0xc0,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x3f,0xc0,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x3f,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x25 (37)
	0x00,0x00,0x3f,0xc0,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x3f,0xc0,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x26 (38)
	0x00,0x00,0x1f,0xc0,0x30,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x61,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x30,0xc0,0x1f,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x27 (39)
	0x00,0x00,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x7f,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x28 (40)
	0x00,0x00,0x7f,0x80,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x7f,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x29 (41)
	0x00,0x00,0x1f,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x61,0x80,0x7f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x2a (42)
	0x00,0x00,0x61,0x80,0x63,0x00,0x66,0x00,0x6c,0x00,0x78,0x00,0x70,0x00,0x78,0x00,0x6c,0x00,0x66,0x00,0x63,0x00,0x61,0x80,0x60,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x2b (43)
	0x00,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x3f,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x2c (44)
	0x00,0x00,0x61,0x80,0x61,0x80,0x73,0x80,0x73,0x80,0x7f,0x80,0x7f,0x80,0x7f,0x80,0x6d,0x80,0x6d,0x80,0x6d,0x80,0x61,0x80,0x61,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x2d (45)
	0x00,0x00,0x60,0xc0,0x70,0xc0,0x70,0xc0,0x78,0xc0,0x78,0xc0,0x6c,0xc0,0x66,0xc0,0x66,0xc0,0x63,0xc0,0x63,0xc0,0x61,0xc0,0x60,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x2e (46)
	0x00,0x00,0x1f,0x00,0x31,0x80,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x31,0x80,0x1f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x2f (47)
	0x00,0x00,0x7f,0x80,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x61,0x80,0x7f,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x30 (48)
	0x00,0x00,0x1f,0x00,0x31,0x80,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x31,0x80,0x1f,0x00,0x06,0x00,0x06,0x00,0x03,0xe0, # Character 0x31 (49)
	0x00,0x00,0x7f,0x00,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x63,0x00,0x7e,0x00,0x66,0x00,0x63,0x00,0x61,0x80,0x61,0x80,0x60,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x32 (50)
	0x00,0x00,0x1f,0x80,0x30,0x00,0x60,0x00,0x60,0x00,0x70,0x00,0x38,0x00,0x0e,0x00,0x03,0x80,0x00,0xc0,0x00,0xc0,0x01,0x80,0x7f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x33 (51)
	0x00,0x00,0xff,0xc0,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x34 (52)
	0x00,0x00,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x60,0xc0,0x3f,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x35 (53)
	0x00,0x00,0xc0,0xc0,0xe0,0xc0,0x61,0x80,0x61,0x80,0x73,0x80,0x33,0x00,0x33,0x00,0x3f,0x00,0x1e,0x00,0x1e,0x00,0x1e,0x00,0x0c,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x36 (54)
	0x00,0x00,0xcc,0xc0,0xcc,0xc0,0xcc,0xc0,0x6d,0x80,0x6d,0x80,0x7f,0x80,0x7f,0x80,0x7f,0x80,0x7f,0x80,0x33,0x00,0x33,0x00,0x33,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x37 (55)
	0x00,0x00,0x31,0x80,0x33,0x00,0x1b,0x00,0x1e,0x00,0x0e,0x00,0x0c,0x00,0x0e,0x00,0x1e,0x00,0x33,0x00,0x33,0x00,0x61,0x80,0x61,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x38 (56)
	0x00,0x00,0x60,0x60,0x30,0xc0,0x30,0xc0,0x19,0x80,0x0f,0x00,0x0f,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x39 (57)
	0x00,0x00,0x7f,0xc0,0x00,0xc0,0x01,0x80,0x03,0x00,0x03,0x00,0x06,0x00,0x0c,0x00,0x18,0x00,0x18,0x00,0x30,0x00,0x60,0x00,0x7f,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x3a (58)
	0x3f,0x80,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x3f,0x80, # Character 0x3b (59)
	0x30,0x00,0x30,0x00,0x18,0x00,0x18,0x00,0x0c,0x00,0x06,0x00,0x06,0x00,0x03,0x00,0x03,0x00,0x01,0x80,0x01,0x80,0x00,0xc0,0x00,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x3c (60)
	0xfe,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0x06,0x00,0xfe,0x00, # Character 0x3d (61)
	0x00,0x00,0x00,0x00,0x0e,0x00,0x0e,0x00,0x1b,0x00,0x1b,0x00,0x31,0x80,0x31,0x80,0x60,0xc0,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x3e (62)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xff,0xc0,0x00,0x00,0x00,0x00, # Character 0x3f (63)
	0x0c,0x00,0x06,0x00,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x40 (64)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1f,0x80,0x31,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x63,0x80,0x3e,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x41 (65)
	0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x7f,0x00,0x71,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x63,0x00,0x7e,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x42 (66)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1f,0x00,0x31,0x80,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x30,0x00,0x1f,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x43 (67)
	0x00,0xc0,0x00,0xc0,0x00,0xc0,0x00,0xc0,0x0f,0xc0,0x18,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x31,0xc0,0x1f,0x40,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x44 (68)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1f,0x00,0x31,0x80,0x61,0x80,0x61,0x80,0x7f,0x80,0x60,0x00,0x60,0x00,0x31,0x80,0x1f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x45 (69)
	0x03,0xe0,0x06,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x7f,0xc0,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x46 (70)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x0f,0xc0,0x18,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x31,0xc0,0x1f,0xc0,0x00,0xc0,0x31,0x80,0x1f,0x00, # Character 0x47 (71)
	0x60,0x00,0x60,0x00,0x60,0x00,0x60,0x00,0x7f,0x00,0x71,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x48 (72)
	0x18,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x78,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x1e,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x49 (73)
	0x01,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x1f,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x01,0x80,0x03,0x00,0x3e,0x00, # Character 0x4a (74)
	0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x31,0x80,0x33,0x00,0x36,0x00,0x3c,0x00,0x38,0x00,0x3c,0x00,0x36,0x00,0x33,0x00,0x31,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x4b (75)
	0x78,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x18,0x00,0x1e,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x4c (76)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xbb,0x80,0xee,0xc0,0xcc,0xc0,0xcc,0xc0,0xcc,0xc0,0xcc,0xc0,0xcc,0xc0,0xcc,0xc0,0xcc,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x4d (77)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x5f,0x00,0x71,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x4e (78)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x1e,0x00,0x33,0x00,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x33,0x00,0x1e,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x4f (79)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x5f,0x00,0x71,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x61,0x80,0x63,0x00,0x7e,0x00,0x60,0x00,0x60,0x00,0x60,0x00, # Character 0x50 (80)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x0f,0xc0,0x18,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x31,0xc0,0x1f,0xc0,0x00,0xc0,0x00,0xc0,0x00,0xc0, # Character 0x51 (81)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x2f,0xc0,0x38,0xc0,0x30,0xc0,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x30,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x52 (82)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x3e,0x00,0x63,0x00,0x60,0x00,0x30,0x00,0x1e,0x00,0x03,0x00,0x01,0x80,0x61,0x80,0x3f,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x53 (83)
	0x00,0x00,0x00,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x3f,0xc0,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x07,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x54 (84)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x30,0xc0,0x31,0xc0,0x1f,0x40,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x55 (85)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x60,0x60,0x60,0x60,0x30,0xc0,0x30,0xc0,0x19,0x80,0x19,0x80,0x0f,0x00,0x0f,0x00,0x06,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x56 (86)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xcc,0xc0,0xcc,0xc0,0xce,0xc0,0x5e,0x80,0x5f,0x80,0x7b,0x80,0x7b,0x80,0x33,0x00,0x33,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x57 (87)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x61,0x80,0x33,0x00,0x1e,0x00,0x0c,0x00,0x0c,0x00,0x1e,0x00,0x33,0x00,0x33,0x00,0x61,0x80,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x58 (88)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x61,0x80,0x61,0x80,0x31,0x80,0x33,0x00,0x1b,0x00,0x1e,0x00,0x0e,0x00,0x0e,0x00,0x0c,0x00,0x0c,0x00,0x18,0x00,0xf0,0x00, # Character 0x59 (89)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x7f,0xc0,0x01,0xc0,0x03,0x80,0x07,0x00,0x0e,0x00,0x1c,0x00,0x38,0x00,0x70,0x00,0x7f,0xc0,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x5a (90)
	0x07,0x80,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x38,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x07,0x80, # Character 0x5b (91)
	0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x5c (92)
	0x78,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x07,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x0c,0x00,0x78,0x00, # Character 0x5d (93)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x3c,0xc0,0x6e,0xc0,0x67,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x5e (94)
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, # Character 0x5f (95)
]