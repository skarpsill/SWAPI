---
title: "SldWorks::GetDocumentDependenciesCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__GetDocumentDependenciesCount.htm"
---

# SldWorks::GetDocumentDependenciesCount

T his
method is obsolete and has been superseded by[SldWorks::IGetDocumentDependenciesCount2](sldworksAPI.chm::/SldWorks/SldWorks__IGetDocumentDependenciesCount2.htm).

Description

This method determines the number of strings returned by the SldWorks::GetDocumentDependencies
method.

Syntax (OLE Automation)

retval = SldWorks.GetDocumentDependenciesCount(
docName, traverseflag, SearchFlag )

(Table)=========================================================

| Input: | (BSTR) docName | Name of the document |
| --- | --- | --- |
| Input: | (long) traverseflag | TRUE to traverse down into all dependent files, FALSE to only the highest
level within the dependencies |
| Input: | (long) SearchFlag | Set this argument to TRUE to use the search rules to find dependencies,
FALSE to search where the documents were last saved |
| Return: | (long) retval | Number of strings returned by SldWorks::GetDocumentDependencies |

Syntax (COM)

status = SldWorks->GetDocumentDependenciesCount(docName,
traverseflag, SearchFlag, &retval)

(Table)=========================================================

| Input: | (BSTR) docName | Name of the document |
| --- | --- | --- |
| Input: | (long) traverseflag | TRUE to traverse down into all dependent files, FALSE to only the highest
level within the dependencies |
| Input: | (long) SearchFlag | Set this argument to TRUE to use the search rules to find dependencies,
FALSE to search where the documents were last saved |
| Output: | (long) retval | Number of strings returned by SldWorks::GetDocumentDependencies |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the SearchFlag is set to TRUE then the current directory is set to
the directory of the docName file. This replicates the interactive behavior
of theReferencesbutton in the
File Open dialog window.

For a complete description of this function and its arguments, see SldWorks::GetDocumentDependencies.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$ZReferences$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\SldWorks\SldWorks__GetDocumentDependenciesCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
