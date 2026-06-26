---
title: "SldWorks::RemoveFileOpenItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__RemoveFileOpenItem.htm"
---

# SldWorks::RemoveFileOpenItem

This method is obsolete and has been superseded
by[SldWorks::RemoveFileOpenItem2](sldworksAPI.chm::/SldWorks/SldWorks__RemoveFileOpenItem2.htm).

Description

This method removes a file type from the File Open list that was added
using SldWorks::AddFileOpenItem. The parameters passed to this method
should match the parameters you used when calling SldWorks::AddFileOpenItem.

Syntax (OLE Automation)

retval = SldWorks.RemoveFileOpenItem
( CallbackFcnAndModule, Description)

(Table)=========================================================

| Input: | (BSTR) CallbackFcnAndModule | Name of module and function used in your call to SldWorks::AddFileOpenItem |
| --- | --- | --- |
| Input: | (BSTR) Description | Description used in your call to SldWorks::AddFileOpenItem |
| Return: | (VARIANT_BOOL) retval | TRUE if successfully removed from the File Type list, FALSE otherwise |

Syntax (COM)

status = SldWorks->RemoveFileOpenItem
( CallbackFcnAndModule, Description, &retval )

(Table)=========================================================

| Input: | (BSTR) CallbackFcnAndModule | Name of module and function used in your call to SldWorks::AddFileOpenItem |
| --- | --- | --- |
| Input: | (BSTR) Description | Description used in your call to SldWorks::AddFileOpenItem |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully removed from the File Type list, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="Items" value="SldWorks_Object$$**$$ZModifyUserInterface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__RecordLine.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
