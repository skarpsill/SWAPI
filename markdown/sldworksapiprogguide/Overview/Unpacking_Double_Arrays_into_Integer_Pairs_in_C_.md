---
title: "Unpacking and Packing Arrays in C#"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Unpacking_Double_Arrays_into_Integer_Pairs_in_C_.htm"
---

# Unpacking and Packing Arrays in C#

Some of the arguments passed from and to SOLIDWORKS using the API
contain arrays of doubles. In some functions, elements in these arrays
contain two integers packed into a double array element. You can unpack
the data from a double to two integers and vice versa.

using System;

using System.Runtime.InteropServices;

namespace WindowsApplication2

{

[StructLayout(LayoutKind.Explicit)]

public struct DoubleIntConv

{

// An 8-byte double contains 2 4-byte ints.

[FieldOffset(0)] private intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}m_Int1;

[FieldOffset(4)] private intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}m_Int2;

[FieldOffset(0)] private double m_Double;

private DoubleIntConv(double dValue)

{

//C# wants these initialized in the constructor

m_Int1 = 0; m_Int2 = 0;

m_Double = dValue;

}

private DoubleIntConv(int iValue1, int iValue2)

{

//C# wants this initialized in the constructor

m_Double = 0.0;

m_Int1 = iValue1; m_Int2 = iValue2;

}

//Usekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}out
parameters, so client code can pass in an uninitialized variable

//Unpack

public static void Unpack (double dIn, out
int iOut1, out int iOut2)

{

DoubleIntConvkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cv;

cv = new DoubleIntConv(dIn);

iOut1 = cv.m_Int1;

iOut2 = cv.m_Int2;

return;

}

//Use an out parameter, so client code
can pass in an uninitialized variable

//Pack

public static void Pack (int iIn1, int iIn2,
out double dOut)

{

DoubleIntConvkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cv;

cv = new DoubleIntConv(iIn1, iIn2);

dOut = cv.m_Double;

return;

}

class Program

{

[STAThread]

static void Main()

{

intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iValueIn1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}= 65535;

intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iValueIn2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}= 0;

doublekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dValueOut;

intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iValueOut1;

intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iValueOut2;

DoubleIntConv.Pack(iValueIn1, iValueIn2,
out dValueOut);

DoubleIntConv.Unpack(dValueOut, out iValueOut1,
out iValueOut2);

return;

}

}

}

See Create
Reference Curve Example (C#) for an example of packing an array.
