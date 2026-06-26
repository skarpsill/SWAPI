---
title: "Modeler::ISplitFaceOnParamCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__ISplitFaceOnParamCount.htm"
---

# Modeler::ISplitFaceOnParamCount

This
method is obsolete and has been superseded by[Modeler::ISplitFaceOnParamCount2](sldworksAPI.chm::/Modeler/Modeler__ISplitFaceOnParamCount2.htm).

Description

This method sets up and counts the number of
new faces split on the U or V parameter

Syntax (OLE Automation)

Not available.

NOTE:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Use the
upper bound on the SafeArray returned from Modeler::SplitFaceOnParam.

Syntax (COM)

status = Modeler->ISplitFaceOnParamCount ( face,
UVFlag, parameter, &retval, &newFaceCount,)

(Table)=========================================================

| Input: | (LPFACE) face | Pointer to the face |
| --- | --- | --- |
| Input: | (long) UVFlag | The parametric axis; either swSplitFaceOnParamU
or swSplitFaceOnParamV |
| Input: | (double) parameter | Position along the parametric axis at which the
split will be performed |
| Output: | (VARIANT_BOOL) retval | TRUE if the operation was successful, FALSE otherwise |
| Output: | (long) newFaceCount | Number of new faces |
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Modeler\Modeler__ISplitFaceOnParamCount.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Modeler\Modeler__ISplitFaceOnParamCount.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
