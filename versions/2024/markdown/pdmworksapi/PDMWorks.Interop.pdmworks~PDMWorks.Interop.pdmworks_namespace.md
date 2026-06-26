---
title: "PDMWorks.Interop.pdmworks Namespace"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "PDMWorks.Interop.pdmworks"
member: ""
kind: "namespace"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks_namespace.html"
---

# PDMWorks.Interop.pdmworks Namespace

SOLIDWORKS Workgroup PDM API

## Interfaces

| Interface | Description |
| --- | --- |
| IPDMWConfiguration | Provides access to SOLIDWORKS configurations. |
| IPDMWConfigurations | Contains IPDMWConfiguration objects. |
| IPDMWConnection | Allows you to log in and out of SOLIDWORKS Workgroup PDM and get projects and documents. |
| IPDMWDocument | Represents and provides access to a single file that is checked into the vault. Some document properties, such as configuration, references, and where used, only work with SOLIDWORKS documents (.sldprt, .sldasm, and .slddrw files). |
| IPDMWDocumentNote | Provides access to notes. |
| IPDMWDocumentNotes | Contains IPDMWDocumentNote objects. |
| IPDMWDocuments | Contains IPDMWDocument objects. |
| IPDMWGroup | Provides access to a group object. Typically, users assigned to the same projects are also assigned to the same group. |
| IPDMWGroups | Provides access to a collection of IPDMWGroup objects. |
| IPDMWLink | Provides access to a link object. A link contains basic information about a referenced document. |
| IPDMWLinks | Contains IPDMWLink objects. |
| IPDMWProject | Provides access to the properties of vault projects. |
| IPDMWProjects | Contains IPDMWProject objects. |
| IPDMWProperties | Contains IPDMWProperty objects. |
| IPDMWProperty | Provides access to a configuration, document, or vault administrator-assigned custom property. |
| IPDMWSearchCriteria | Provides access to search criteria to locate documents in the vault. |
| IPDMWSearchOptions | Provides access to search criteria options. |
| IPDMWSearchResult | Provides access to search results. |
| IPDMWSearchResults | Contains IPDMWSearchResult objects. |
| IPDMWUser | Provides access to a user record. |
| IPDMWUsers | Provides access to a collection of user records. |

## Enumerations

| Enumeration | Description |
| --- | --- |
| PDMWAndOr | Logical operators for subsequent search criteria |
| PDMWChildrenType | Types of children documents |
| PDMWConditionType | Search conditions |
| PDMWLinkType | Types of links |
| PDMWPermission | Read and write permissions for projects |
| PDMWPropertyType | Property types |
| PDMWRevisionOptionType | Revision options |

## See Also

[PDMWorks.Interop.pdmworks Assembly](PDMWorks.Interop.pdmworks.html)
