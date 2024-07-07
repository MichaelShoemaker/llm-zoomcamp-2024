#Data Retreived From https://aa.usno.navy.mil/data/RS_OneYear
import pandas as pd

data = """
01  0718 1630  0704 1705  0625 1742  0533 1817  0446 1850  0418 1920  0420 1929  0445 1908  0517 1823  0548 1731  0624 1644  0659 1620
02  0718 1631  0702 1707  0623 1743  0531 1818  0445 1851  0417 1921  0420 1929  0446 1907  0518 1821  0549 1730  0625 1643  0700 1620
03  0718 1632  0701 1708  0621 1744  0529 1819  0444 1852  0417 1921  0421 1929  0447 1906  0519 1820  0550 1728  0626 1642  0701 1620
04  0718 1633  0700 1709  0620 1745  0528 1820  0442 1853  0417 1922  0421 1929  0448 1905  0520 1818  0551 1726  0627 1641  0702 1620
05  0718 1634  0659 1711  0618 1746  0526 1821  0441 1854  0416 1923  0422 1929  0449 1903  0521 1816  0553 1725  0629 1639  0703 1620
06  0718 1635  0658 1712  0617 1748  0524 1822  0440 1855  0416 1923  0423 1928  0450 1902  0522 1815  0554 1723  0630 1638  0704 1620
07  0718 1636  0657 1713  0615 1749  0523 1823  0439 1856  0416 1924  0423 1928  0451 1901  0523 1813  0555 1721  0631 1637  0705 1620
08  0718 1637  0656 1714  0613 1750  0521 1825  0438 1857  0416 1924  0424 1927  0452 1900  0524 1811  0556 1720  0632 1636  0706 1620
09  0718 1638  0655 1716  0612 1751  0519 1826  0436 1858  0415 1925  0425 1927  0453 1858  0525 1810  0557 1718  0634 1635  0707 1620
10  0718 1639  0653 1717  0610 1752  0518 1827  0435 1900  0415 1926  0426 1927  0454 1857  0526 1808  0558 1716  0635 1634  0708 1620
11  0717 1640  0652 1718  0608 1753  0516 1828  0434 1901  0415 1926  0426 1926  0455 1856  0527 1806  0559 1715  0636 1633  0709 1620
12  0717 1641  0651 1720  0607 1755  0514 1829  0433 1902  0415 1927  0427 1926  0456 1854  0528 1804  0600 1713  0637 1632  0709 1620
13  0717 1642  0650 1721  0605 1756  0513 1830  0432 1903  0415 1927  0428 1925  0457 1853  0529 1803  0601 1711  0639 1631  0710 1620
14  0716 1643  0648 1722  0603 1757  0511 1831  0431 1904  0415 1927  0429 1924  0459 1851  0530 1801  0603 1710  0640 1630  0711 1620
15  0716 1644  0647 1723  0602 1758  0510 1832  0430 1905  0415 1928  0429 1924  0500 1850  0531 1759  0604 1708  0641 1629  0712 1620
16  0716 1646  0646 1725  0600 1759  0508 1833  0429 1906  0415 1928  0430 1923  0501 1848  0533 1757  0605 1707  0642 1629  0712 1621
17  0715 1647  0644 1726  0558 1800  0506 1835  0428 1907  0415 1928  0431 1922  0502 1847  0534 1756  0606 1705  0643 1628  0713 1621
18  0714 1648  0643 1727  0556 1801  0505 1836  0427 1908  0415 1929  0432 1922  0503 1845  0535 1754  0607 1704  0645 1627  0714 1622
19  0714 1649  0641 1728  0555 1802  0503 1837  0426 1909  0415 1929  0433 1921  0504 1844  0536 1752  0608 1702  0646 1626  0714 1622
20  0713 1650  0640 1730  0553 1804  0502 1838  0426 1910  0416 1929  0434 1920  0505 1842  0537 1750  0609 1701  0647 1626  0715 1623
21  0713 1652  0638 1731  0551 1805  0500 1839  0425 1910  0416 1929  0435 1919  0506 1841  0538 1749  0610 1659  0648 1625  0715 1623
22  0712 1653  0637 1732  0549 1806  0459 1840  0424 1911  0416 1930  0436 1918  0507 1839  0539 1747  0612 1658  0649 1624  0716 1624
23  0711 1654  0636 1733  0548 1807  0457 1841  0423 1912  0416 1930  0436 1917  0508 1838  0540 1745  0613 1656  0650 1624  0716 1624
24  0711 1655  0634 1734  0546 1808  0456 1842  0423 1913  0417 1930  0437 1917  0509 1836  0541 1743  0614 1655  0652 1623  0716 1625
25  0710 1657  0632 1736  0544 1809  0455 1843  0422 1914  0417 1930  0438 1916  0510 1835  0542 1742  0615 1653  0653 1623  0717 1625
26  0709 1658  0631 1737  0543 1810  0453 1844  0421 1915  0417 1930  0439 1915  0511 1833  0543 1740  0617 1652  0654 1622  0717 1626
27  0708 1659  0629 1738  0541 1811  0452 1846  0421 1916  0418 1930  0440 1914  0512 1831  0544 1738  0618 1651  0655 1622  0717 1627
28  0707 1700  0628 1739  0539 1812  0450 1847  0420 1917  0418 1930  0441 1913  0513 1830  0545 1736  0619 1649  0656 1621  0718 1628
29  0706 1702  0626 1741  0538 1814  0449 1848  0419 1917  0419 1930  0442 1912  0514 1828  0546 1735  0620 1648  0657 1621  0718 1628
30  0705 1703  0000 0000  0536 1815  0448 1849  0419 1918  0419 1930  0443 1910  0515 1826  0547 1733  0621 1647  0658 1621  0718 1629
31  0705 1704  0000 0000  0534 1816  0000 0000  0418 1919  0000 0000  0444 1909  0516 1825  0000 0000  0623 1645  0000 0000  0718 1630"""

# Split the data into lines and then split each line into parts
lines = data.split('\n')
clean_lines = []
for line in lines:
    if len(line) > 5:
        line = line.replace('             ','  0000 0000  ')
        clean_lines.append(line)


parsed_data = [line.split() for line in lines]

# Define the months and initialize a list to store the structured data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
structured_data = []

# Process each line of the parsed data
for line in parsed_data:
    if len(line) != 25:
        print(line)
        print("Data format error: Skipping line.")
        continue
    day = line[0]
    for i in range(12):
        month = months[i]
        rise = line[1 + 2 * i]
        set_ = line[2 + 2 * i]
        structured_data.append({'month': f'{month}-{day}', 'rise': rise, 'set': set_})

# Create the DataFrame
df = pd.DataFrame(structured_data)

# Display the DataFrame
print(df)