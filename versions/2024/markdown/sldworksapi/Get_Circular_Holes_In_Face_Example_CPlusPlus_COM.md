---
title: "Get Circular Holes In Face Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Circular_Holes_In_Face_Example_CPlusPlus_COM.htm"
---

# Get Circular Holes In Face Example (C++ COM)

This example shows how to calculate the number
of circular holes in a selected face.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}IEdge::IGetCurveParams2
and ILoop::IGetEdges return arrays, so this code must be used in an in-process
DLL. Otherwise, use the methods IEdge::GetCurveParams2 and IEdge::GetEdges
that return VARIANTs.

void GetCountHole1(LPMODELDOC2 pModelDoc, CString* Message)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
lres=0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
pCount=0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPSELECTIONMGR
pSelectMgr=NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULT
hres=NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPUNKNOWN
pUnk=NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPFACE
SelectedFace=NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPLOOP
pLoop=NULL,pFirstLoop=NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOL
pVBool,pCBool;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPEDGE
pEdge=NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPCURVE
pCurve=NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}char
ch[128];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}short
i;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
pEdgeCount;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Form
the return message

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message
= "";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Get
the selection mgr for this doc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK!=pModelDoc->get_ISelectionManager(&pSelectMgr)||pSelectMgr==NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="Unable
to get the Selection Manager.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

else if(S_OK!=pSelectMgr->GetSelectedObjectType(1,&lres)||lres==0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Get
the selected object type

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="No
face is currently selected.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if(S_OK!=pSelectMgr->IGetSelectedObject2(1,&pUnk)||pUnk==NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Get
the selected object of Unknown Type

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="Unable
to get the selected object.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if(S_OK!=pUnk->QueryInterface(IID_IFace, (LPVOID *)&SelectedFace)||SelectedFace==NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Get
the selected face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="Unable
to get the selected face.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if(S_OK!=SelectedFace->IGetFirstLoop(&pLoop)||pLoop==NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Get
the selected loop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="Unable
to get the selected face first loop.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pFirstLoop=pLoop;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}do

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK!=pLoop->IsOuter(&pVBool)||pVBool==TRUE)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Check
whether the loop is outer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="The
loop is an outer loop.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if(S_OK!=pLoop->GetEdgeCount(&pEdgeCount)||pEdgeCount<=0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Check
the loop has edges, for example, no vertex loops.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="The
loop has no edges.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Allocate
the calculated size edge list array and set them to null

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPEDGE
*pEdgeList = new LPEDGE[pEdgeCount];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i=0;i<pEdgeCount;i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pEdgeList[i]=NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Get
the edge list

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK!=pLoop->IGetEdges(&pEdgeList)||*pEdgeList==NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="Cannot
get the loop edges.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Allocate
the fixed size edge data array

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double*
pEdgeData = new double[100];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Get
the first edge in the list

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pEdge=pEdgeList[0];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK!=pEdge->IGetCurve(&pCurve)||pCurve==NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Get
the curve

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="Cannot
get the edge curve.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
if(S_OK!=pEdge->IGetCurveParams2(&pEdgeData[0]))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Get
the data of curve

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="Failed
to get the curve parameters.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Get
the edge curve data

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(S_OK!=pCurve->IsCircle(&pCBool)||pCBool==FALSE)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the
curve is not a circle

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="The
curve is not a circle.\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Increment
the circular hole count

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else
pCount=pCount+1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Release
the curve

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(pCurve!=NULL)pCurve->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
pEdgeData;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Release
the allocated SOLIDWORKS edge list objects

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i=0;i<pEdgeCount;i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(pEdgeList[i]!=NULL)pEdgeList[i]->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
pEdgeList;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Get
the next loop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}while(S_OK==pLoop->IGetNext(&pLoop)&&pLoop!=NULL&&pLoop!=pFirstLoop);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
t=sprintf(ch,"%d",pCount);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CString
pStr(ch);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*Message+="The
number of circular holes is " + pStr + ".\r\n";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

// Everything is okay.

// ========== == ===== =====

// Release the loop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(pLoop!=NULL)pLoop->Release();

// Release the selected face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(SelectedFace!=NULL)SelectedFace->Release();

// Release the Selection Manager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(pSelectMgr!=NULL)pSelectMgr->Release();

// Release the unknown object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(pUnk!=NULL)pUnk->Release();

// Return with report of results including errors

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

}
