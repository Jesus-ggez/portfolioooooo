import { Col as RightCol} from "./components/right-col/Col";
import { Col as LeftCol } from "./components/left-col/Col";
import { Bar as TopBar } from "./components/top-bar/Bar";


import './styles/bg-colors.css';
import './styles/bordered.css';
import './styles/li-items.css';
import './styles/boxed.css';
import './styles/sizes.css';
import './styles/axis.css';

export const Layout = () => {
    return (
        <>
            <TopBar />
            <div className="h">
                <LeftCol />
                <RightCol />
            </div>
        </>
    );
}

