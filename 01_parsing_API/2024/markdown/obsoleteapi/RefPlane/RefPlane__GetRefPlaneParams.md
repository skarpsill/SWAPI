---
title: "RefPlane::GetRefPlaneParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RefPlane/RefPlane__GetRefPlaneParams.htm"
---

# RefPlane::GetRefPlaneParams

This method is obsolete and has been superseded
by[RefPlane::Transform](sldworksAPI.chm::/RefPlane/RefPlane__Transform.htm).

Description

This method retrieves information about a reference plane.

Syntax (OLE Automation)

retval = RefPlane.GetRefPlaneParams
()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing an array of doubles (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = RefPlane->IGetRefPlaneParams
( retval )

(Table)=========================================================

| Output: | (double*) retval | Pointer to an array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

To get the RefPlane interface, you must get the reference plane as a
feature, and then use Feature::GetSpecificFeature to return the RefPlane
object.

The return value is the following array of doubles:

[Origin[3],
Xvector[3], NormalVector[3]]

(Table)=========================================================

| Where... | Is an array of three values describing... |
| --- | --- |
| Origin[3] | x,y,z origin of the reference plane. This value locates the model origin
in relation to the coordinate system of the plane. The value is in terms
of the reference planes coordinate system. |
| Xvector[3] | x-axis vector of the reference plane. |
| NormalVector[3] | normal vector of the reference plane. |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="RefPlane_Object$$**$$ZGetInfoRefObjects$$**$$ZCreateRefPlane$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\RefPlane\RefPlane__GetRefPlaneParams.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get_Parameters_of_a_Reference_Plane_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\RefPlane\RefPlane__GetRefPlaneParams.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
