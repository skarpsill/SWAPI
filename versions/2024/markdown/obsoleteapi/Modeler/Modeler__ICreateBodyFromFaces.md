---
title: "Modeler::ICreateBodyFromFaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__ICreateBodyFromFaces.htm"
---

# Modeler::ICreateBodyFromFaces

This method is obsolete and has been superceded
by[Modeler::ICreateBodyFromFaces3](sldworksAPI.chm::/Modeler/MODELER__ICREATEBODYFROMFACES3.HTM).

Description

This method creates a temporary body from a
list of faces.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Modeler->ICreateBodyFromFaces ( numFaces,
faceList, doLocalCheck, localCheckResult, &retval )

(Table)=========================================================

| Input: | (long) numFaces | Number of Face objects in the faceList array |
| --- | --- | --- |
| Input: | (LPFACE* )faceList | Array of Face objects to be sewn |
| Input: | (VARIANT_BOOL) doLocalCheck | TRUE if you want to perform local checking on
the resulting body, FALSE if not |
| Output: | (VARIANT_BOOL) localCheckResult | If doLocalCheck is TRUE and body is okay, then
TRUE, otherwise FALSE |
| Output: | (LPBODY) retval | Pointer to a newly created Body object or NULL
if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Modeler_Object$$**$$ZSewingRoutinesNEW$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Modeler\Modeler__ICreateBodyFromFaces.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
