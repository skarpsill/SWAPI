---
title: "ModelDoc::IGetVersionHistoryCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IGetVersionHistoryCount.htm"
---

# ModelDoc::IGetVersionHistoryCount

This
method is obsolete and has been superseded by[ModelDoc2::IGetVersionHistoryCount](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IGetVersionHistoryCount.htm).

Description

This methodreturns
the size of the array required to hold data returned by[ModelDoc::IVersionHistory](ModelDoc__VersionHistory.htm).

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = ModelDoc->IGetVersionHistoryCount
( &retval )

(Table)=========================================================

| Output: | (int)retval | Size of array required for the version history |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the document has not yet been saved, there is no version history
information and this method will return 0.

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
<param name="Items" value="ModelDoc_Object$$**$$ZFileOperations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__IGetVersionHistoryCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
