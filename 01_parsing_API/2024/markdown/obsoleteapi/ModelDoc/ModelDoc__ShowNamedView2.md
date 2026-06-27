---
title: "ModelDoc::ShowNamedView2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ShowNamedView2.htm"
---

# ModelDoc::ShowNamedView2

This method is obsolete
and has been superseded by[ModelDoc2::ShowNamedView2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ShowNamedView2.htm).

Description

This method displays the specified view.

Syntax (OLE Automation)

void ModelDoc.ShowNamedView2 ( vName,
viewId)

(Table)=========================================================

| Input: | (BSTR) vName | Name of the view to be displayed or an empty string if you wish to use
the viewId argument instead |
| --- | --- | --- |
| Input: | (long) viewId | ID of the view to be displayed or -1 if you wish to use the viewName
argument instead; if you specify both the viewName and viewId, then viewId
takes precedence if the two arguments do not resolve to the same view |

Syntax (COM)

status = ModelDoc->ShowNamedView2
( vName, viewId )

(Table)=========================================================

| Input: | (BSTR) vName | Name of the view to be displayed or an empty string if you wish to use
the viewId argument instead |
| --- | --- | --- |
| Input: | (long) viewId | ID of the view to be displayed or -1 if you wish to use the viewName
argument instead; if you specify both the viewName and viewId, then viewId
takes precedence if the two arguments do not resolve to the same view |
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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__ShowNamedView2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
