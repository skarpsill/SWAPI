---
title: "Get Sketch Spline Parameters Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Sketch_Get_Spline_Parameters_Example_CPlusPlus_COM.htm"
---

# Get Sketch Spline Parameters Example (C++ COM)

This example shows how to get splines parameter
data from sketches and how to unpack that data.

The method ISketch::IGetSplineParams2 returns
an array, so this code must be used in an in-process DLL. Otherwise, use
the method ISketch::GetSplineParams2 that returns a VARIANT.

// Union for use unpacking the data in the first two array
elements for each spline

union SplinePackedData

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
doublevalue[2];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intvalue[4];

};

void GetSketchSplines(LPSKETCH pSketch,CString* Message)

{

// Assume that pSketch has been set to a valid sketch
already

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CStringkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Text;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DataSize,
NoSplines;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the spline parameters

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK
!= pSketch->GetSplineParamsCount(&DataSize,
&NoSplines) )return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(NoSplines==0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
+= " Has no spline curves\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData
= (double*)malloc(sizeof(double) * DataSize);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK
!= pSketch->IGetSplineParams2(pData)
)return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Format the spline parameter data

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ExtractSplineData
( DataSize, pData, Message );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

//////////////////////////////////////////////////////////////////////////

// Method: ExtractSplinesData

// Arguments: DataSize - Size of the array containing
the splines parameters

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pData
- Data array containing splines parameters

// Return: Message - A CString for returning the formatted
information

// Description:Extract the splines parameter data returned

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}from
GetSplineParams and format it into a

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
for display.

//////////////////////////////////////////////////////////////////////////

void CGetSketchesApp::ExtractSplinesData(int DataSize,
double* pData, CString* Message)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Index
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Order;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nCtrlPoints;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Periodic;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nKnots;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}doublekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Knot;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SplinePackedData*
pPackedData;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}intkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i,j;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CStringkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Line;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

// Continue until all the data is processed, i.e. 1 loop
per spline

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}while
( Index < DataSize )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Unpack the information about the spline

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPackedData
= (SplinePackedData*)&pData[Index];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
= pPackedData->intvalue[0];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Order
= pPackedData->intvalue[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nCtrlPoints
= pPackedData->intvalue[2];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Periodic
= pPackedData->intvalue[3];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nKnots
= Periodic ? nCtrlPoints+1 : nCtrlPoints+Order;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Format Text

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Line.Format(_T("Spline\r\nDimension
%d\r\nNumControlPoints %d\r\n

Num of Knots %d\r\nPeriodic %d\r\n"),Dim, nCtrlPoints,
nKnots, Periodic);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
+= Line;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Extract Control points

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Index+=2;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Step past packed data

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
( i=0; i<nCtrlPoints; i++ )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Assume 3 dimensions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
CtrlPoint[3];kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
( j=0; j<3; j++ )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CtrlPoint[j]
= pData[Index++];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Format text (in this case assume 3 dimensions)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Line.Format(_T("Control
Point: %lf %lf %lf\r\n"),

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CtrlPoint[0],

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CtrlPoint[1],

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CtrlPoint[2]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
+= Line;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Extract Knots

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
( i=0; i<nKnots; i++ )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Knot
= pData[Index++];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Format text

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Line.Format(_T("Knot:
%lf\r\n"), Knot);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
+= Line;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
