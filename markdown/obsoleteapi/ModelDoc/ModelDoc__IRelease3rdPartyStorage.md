---
title: "ModelDoc::IRelease3rdPartyStorage"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IRelease3rdPartyStorage.htm"
---

# ModelDoc::IRelease3rdPartyStorage

This
method is obsolete and has been superseded by[ModelDoc2::IRelease3rdPartyStorage](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IRelease3rdPartyStorage.htm).

Description

This method
closes the specified storage stream.

Syntax (OLE Automation)

Not Available.

Syntax (COM)

status = ModelDoc-> IRelease3rdPartyStorage(
stringIn )

(Table)=========================================================

| Input: | (BSTR) stringIn | Name of the storage stream to close |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method with[ModelDoc::IGet3rdPartyStorage](ModelDoc__IGet3rdPartyStorage.htm)f you are not using the LoadFromStorageNotify event. You need must call
this method even when the call to ModelDoc::IGet3rdPartyStorage returns
a NULL stream. For more information, see ModelDoc::IGet3rdPartyStorage.

NOTE:If you are using serialization, then you should be careful with
the standard MFC macros; otherwise, you might get messages likeUnexpected File Formatafter your application
is unloaded. One way of using IMPLEMENT_SERIAL is:

IMPLEMENT_SERIAL( CCustomAttr, CObject, VERSIONABLE_SCHEMA|0 )

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
<param name="Items" value="ModelDoc_Object$$**$$ZFileStorageOperations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__IRelease3rdPartyStorage.htm" >
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
<param name="Items" value="Storage$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__IRelease3rdPartyStorage.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
