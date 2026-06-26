---
title: "ModelDoc::VersionHistory"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__VersionHistory.htm"
---

# ModelDoc::VersionHistory

This method is obsolete
and has been superseded by[ModelDoc2::VersionHistory](sldworksAPI.chm::/ModelDoc2/ModelDoc2__VersionHistory.htm).

Description

This method returns a list of strings indicating the versions in which
this document was saved.

Syntax (OLE Automation)

retval = ModelDoc.VersionHistory (
)

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing an array of strings of the version
history |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IVersionHistory
( retval )

(Table)=========================================================

| Output: | (BSTR*) retval | An array of strings containing the version history |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

There is one array entry for each major release of SolidWorks in which
the document has been saved. The format for each entry is a major release
code followed by one or more minor release codes separated by commas:

"<major release code>[<minor release code>]" or

"<major release code>[<minor release code>,<minor
release code>...]"

where:

<major release code> = a number that remains constant through
a major release of SolidWorks. For example, the following values would
be returned based on the corresponding major SolidWorks version:

SolidWorks 95 = 44

SolidWorks 96 = 243

SolidWorks 97 = 483

SolidWorks 97Plus = 629

SolidWorks 98 = 822

SolidWorks 98Plus = 1008

SolidWorks 99 = 1137

SolidWorks 2000 = 1500

<minor release
code> = the year and day of manufacture of a saving version (for example,
1997/320)

To get the size of array needed by IVersionHistory call ModelDoc::IGetVersionHistoryCount.

NOTE:If the document has not
yet been saved, there is no version history information. In that case,
this method (OLE Automation) returns VT_EMPTY, and the ModelDoc::IGetVersionHistoryCount
API (COM) returns 0.

Last value returned in this array is the active
SolidWorks version.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\ModelDoc\ModelDoc__VersionHistory.htm" >
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
<param name="Items" value="ZExample_DocumentVersionHistory$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\ModelDoc\ModelDoc__VersionHistory.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
