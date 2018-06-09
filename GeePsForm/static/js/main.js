const divTip = document.getElementById("helpHostID");
const selectedLanguage = document.getElementById("language");
const selectedOS = document.getElementById("os");

function findHostID() {
	let language = selectLanguage.value;
	const os = selectedOS.value;
	if (language === "fr") {
		if (os === "windows") {
			divTip.innerHTML = "Windows\n\n"
			+ /*premiere partie a traduire*/"For Network Concurrent or Network Named User licenses, l'addresse MAC doit etre utilisée en tant qu'host ID."
			+ "De plus, les ordinateurs avec un disque B: doivent utiliser l'addresse MAC en tant qu'host ID.\n\n"
			+ "Pour obtenir l'addresse MAC de votre ordinateur, lancez l'invite de commandes Windows et executez la commande suivante:\n\n"
			+ "getmac";
		} else if (os === "linux") {
			// TODO: translation
			
		} else {
			// Mac
			divTip.innerHTML = "MacOS\n\nSur Mac, l'host ID correspond à l'addresse MAC de l'appareiol en0.\n\n" 
			+ "Pour obtenir l'addresse MAC de l'appareil en0, commencez par ouvrir un terminal:\n\n"
			+ "Ouvrez Finder\nOuvrez le répertoire \"Applications\"\n"
			+ "Ouvrez le répertoire \"Utilities\"\n"
			+ "Lancez l'application \"Terminal\"\n\n"
			+ "Dans la fenetre du Terminal, entrez les commandes suivantes:\n"
			+ "ifconfig en0 | grep ether\n"
			+ "L'addresse MAC est la valeur listée à coté de \"ether\".\n";
		}
	} else {
		if (os === "windows") {
			divTip.innerHTML = "Windows\n\n"
			+ "For Network Concurrent or Network Named User licenses, the MAC address must be used as the Host ID."
			+ "Additionally, computers with a B: drive must use the MAC address as the host ID.\n\n"
			+ "To obtain the MAC address, open a Windows command prompt and run the following command:\n\n"
			+ "getmac";
		} else if (os === "linux") {
			divTip.innerHTML = "Linux\n\n"
			+ "With R2014a and later, any MAC address can serve as the host ID regardless of interface name. "
			+ "If the interfaces are enumerated, use the lowest-enumerated interface.\n\n"
			+ "To obtain the MAC address using a bash shell, run the following command:\n\n"
			+ "/sbin/ifconfig <interfaceName>\n\n"
			+ "Where <interfaceName> is the name of the network interface. For example, en0, eth0, wlan0, or enp5s0 "
			+ "are common Linux network interface names, although this will vary from computer to computer.\n\n"
			+ "For R2013b and earlier, the Host ID is the MAC address of the eth0 or en0 interface.\n\n"
			+ "To obtain the MAC Address using a bash shell, run the following command:\n\n"
			+ "/sbin/ifconfig eth0\n\n"
			+ "or\n\n"
			+ "/sbin/ifconfig eth1\n\n"
			+ "The MAC Address is usually the value listed next to \"HWaddr\". "
			+ "If your Linux distribution does not have network interfaces which follow the enX or ethX naming scheme, "
			+ "you will either need to update to MATLAB R2014a or later, or change the name of your interfaces so MATLAB "
			+ "can detect them. Consult your distribution's documentation for instructions on changing the network"
			+ "interface naming scheme.\n";
		} else {
			// Mac
			divTip.innerHTML = "MacOS\n\nFor MacOS, the Host ID is the MAC address of the en0 device.\n\n" 
			+ "To obtain the MAC address of the en0 device, start by opening a Terminal window:\n\n"
			+ "Open Finder\nOpen the \"Applications\" folder\n"
			+ "Open the \"Utilities\" folder\n"
			+ "Start the \"Terminal\" application\n\n"
			+ "In the Terminal window, enter the following command:\n"
			+ "ifconfig en0 | grep ether\n"
			+ "The MAC address is the value listed next to \"ether\".\n";
		}	
	}
}