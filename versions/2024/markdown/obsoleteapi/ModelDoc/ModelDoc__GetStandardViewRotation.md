---
title: "ModelDoc::GetStandardViewRotation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetStandardViewRotation.htm"
---

# ModelDoc::GetStandardViewRotation

This method is obsolete
and has been superseded by[ModelDoc2::GetStandardViewRotation](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IGetStandardViewRotation.htm).

Description

This method gets the specified view orientation matrix with respect
to the Front view. Be aware that the user may have redefined the Front
view to be something other than the X-Y plane.

Syntax (OLE Automation)

retval = ModelDoc.GetStandardViewRotation
( viewId)

(Table)=========================================================

| Input: | (long) viewId | View ID to evaluate as defined in swStandardViews_e |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray describing the view rotation with respect
to the Front view; this is an array of 9 doubles |

Syntax (COM)

status = ModelDoc->IGetStandardViewRotation
( viewId, retval )

(Table)=========================================================

| Input: | (long) viewId | View ID to evaluate as defined in swStandardViews_e |
| --- | --- | --- |
| Output: | (double*) retval | Pointer to an array of 9 doubles describing the view rotation with respect
to the Front view |
| Return: | (HRESULT) status | S_OK if successful |

RemarksMetadata type="DesignerControl" startspan
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
<param name="Items" value="ModelDoc_Object$$**$$ZGetInfoModelView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetStandardViewRotation.htm" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get_Standard_View_Rotation_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetStandardViewRotation.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
