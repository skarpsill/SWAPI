---
title: "Modeler::ICheckInterferenceCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__ICheckInterferenceCount.htm"
---

# Modeler::ICheckInterferenceCount

This
method is obsolete and has been superceded by[Modeler::ICheckInterferenceCount2](sldworksAPI.chm::/Modeler/Modeler__ICheckInterferenceCount2.htm).

Description

This method checks interference between two
temporary bodies and returns the number of interferences.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Modeler->ICheckInterferenceCount ( body1,
body2, coincidentInterference, *body1InterferedFaceCount, *body2InterferedFaceCount,
*intersectedBodyCount, &retval )

(Table)=========================================================

| Input: | (LPBODY) body1 | Pointer to a body object to check for interference. |
| --- | --- | --- |
| Input: | (LPBODY) body2 | Pointer to another body object to check for interference |
| Input: | (VARIANT_BOOL) coincidentInterference | TRUE to check for coincident interference, FALSE
otherwise |
| Output: | (long) *body1InterferedFaceCount | Number of faces that are interfering that belong
to the body passed in the first parameter of this method |
| Output: | (long) *body2InterferedFaceCount | Number of faces that are interfering that belong
to the body passed in the second parameter of this method |
| Output: | (long) *intersectedBodyCount | Number of intersection bodies produced from this
intersection |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call Modeler::ICheckInterference after calling
this method.

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
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Modeler\Modeler__ICheckInterferenceCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="Items" value="Modeler_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Modeler\Modeler__ICheckInterferenceCount.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
