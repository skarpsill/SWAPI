---
title: "Modeler::CreateBodyFromBox"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__CreateBodyFromBox.htm"
---

# Modeler::CreateBodyFromBox

This method is obsolete and has been superseded
by[Modeler::CreateBodyFromBox3](sldworksAPI.chm::/Modeler/Modeler__CreateBodyFromBox3.htm).

Description

This method creates a temporary body from box dimensions.

Syntax (OLE Automation)

retval = Modeler.CreateBodyFromBox
( boxDimArray)

(Table)=========================================================

| Input: | (VARIANT) boxDimArray | VARIANT of type SafeArray of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the resulting body |

Syntax (COM)

This method is obsolete
and has been superseded byModeler::ICreateBodyFromBox2.

status = Modeler->ICreateBodyFromBox (
boxDimArray, &retval )

(Table)=========================================================

| Input: | (double*) boxDimArray | Pointer to an array of 9 doubles |
| --- | --- | --- |
| Output: | (LPBODY*) retval | Pointer to the resulting body |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The input parameter is the following array of doubles:

[boxFaceCenter[3],boxAxis[3],boxWidth, boxLength,boxHeight]

where:

(Table)=========================================================

| boxFaceCenter [3] | XYZ location that represents the center of one of the box faces. |
| --- | --- |
| boxAxis [3] | XYZ direction. The box will be extruded along this vector from the boxFaceCenter location , a distance of boxHeight. |
| boxWidth | Box width. If boxAxis is parallel
to the Z axis (0,0,1), then this value represents the dimension that is
parallel to the X-axis; otherwise, the orientation is not defined. |
| boxLength | Box length. If boxAxis is parallel
to the Z axis (0,0,1), then this value represents the dimension that is
parallel to the Y axis; otherwise, the orientation is not defined. |
| boxHeight | Height to extrude along the boxAxis direction. If boxHeight is 0,
a sheet body will be created of dimension boxWidth x boxLength and whose normal
is defined by boxAxis . |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Modeler_Object$$**$$ZAccessorByCreate$$**$$ZCreateTemporaryBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Modeler\Modeler__CreateBodyFromBox.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXCreateSolidBodyGeometryTopology$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Modeler\Modeler__CreateBodyFromBox.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
